import pydantic


class RAGChunkandSRC(pydantic.BaseModel):
    chunks: list[str]
    source_id: str=None


class RAGUpsertResults(pydantic.BaseModel):
    ingested:int

class RAGSearchResult(pydantic.BaseModel):
    contexts:list[str]
    sources:list[str]

class RAGQueryResult(pydantic.BaseModel):
    answers:str
    sources:list[str]
    num_contexts : int
