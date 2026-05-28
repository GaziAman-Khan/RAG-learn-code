import logging
from fastapi import FastAPI
import inngest
import inngest.fast_api
from dotenv import load_dotenv
from google import genai
import uuid
import os
import datetime
from inngest.experimental import ai
from data_loader import load_and_chunk_pdf, embed_texts
from vector_db import QdrantStorage
from custom_type import RAGChunkandSRC, RAGQueryResult, RAGSearchResult, RAGUpsertResults

load_dotenv()

inngest_client = inngest.Inngest(
    app_id="rag_app",
    logger=logging.getLogger("uvicorn"),
    is_production=False,
    serializer=inngest.PydanticSerializer(),
)

@inngest_client.create_function(
    fn_id="RAG: Inngest PDF",
    trigger=inngest.TriggerEvent(event="rag/inngest_pdf"),
)
async def rag_inngest_pdf(ctx: inngest.Context):
    def _load(ctx:inngest.Context) -> RAGChunkandSRC:
        pdf_path=ctx.event.data["pdf_path"]
        source_id = ctx.event.data.get("source_id", pdf_path)
        chunks = load_and_chunk_pdf(pdf_path)
        return RAGChunkandSRC(chunks= chunks, source_id=source_id)

    def _upsert(chunks_and_src) -> RAGUpsertResults:
        chunks = chunks_and_src.chunks
        source_id = chunks_and_src.source_id
        vecs = embed_texts(chunks)
        ids = [str(uuid.uuid5(uuid.NAMESPACE_URL, name= f"{source_id}:{i}")) for i in range(len(chunks))]
        payload = [{"source": source_id, "text": chunks[i]} for i in range(len(chunks))]
        QdrantStorage().upsert(ids,vecs,payload)
        return RAGUpsertResults(ingested=len(chunks))

    chunks_and_src = await ctx.step.run("load-and-chunk", lambda:_load(ctx), output_type=RAGChunkandSRC)
    ingested = await ctx.step.run("embed-and-upsert", lambda:_upsert(chunks_and_src), output_type=RAGUpsertResults)
    return ingested.model_dump()

@inngest_client.create_function(
    fn_id ="RAG:Query PDF",
    trigger=inngest.TriggerEvent(event="rag/query_pdf_ai")
)

async def rag_query_pdf_ai(ctx: inngest.Context):
    def _search(question: str, top_k: int = 5) -> RAGSearchResult:
        query_vec = embed_texts([question])[0]
        store = QdrantStorage()
        found = store.search(query_vec, top_k)
        return RAGSearchResult(
            contexts=found["contexts"],
            sources=found["sources"]
        )

    question = ctx.event.data["question"]
    top_k = int(ctx.event.data.get("top_k", 5))

    found = await ctx.step.run(
        "embed-and-search",
        lambda: _search(question, top_k),
        output_type=RAGSearchResult
    )

    context_block = "\n\n".join(f"- {c}" for c in found.contexts)

    user_context = (
        "Use the following context to answer the question.\n\n"
        f"Context:\n{context_block}\n\n"
        f"Question: {question}\n"
        "Answer concisely using the context above."
    )

    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=(
            "You answer questions using only the provided context.\n\n"
            + user_context
        )
    )

    answer = response.text.strip()

    return {
        "answers": answer,
        "source": found.sources,
        "num_contexts": len(found.contexts)
    }

app = FastAPI()

@app.get("/")
def home():
    return {"messages": "API is running"}

inngest.fast_api.serve(
    app,
    inngest_client,
    functions=[rag_inngest_pdf, rag_query_pdf_ai]
)