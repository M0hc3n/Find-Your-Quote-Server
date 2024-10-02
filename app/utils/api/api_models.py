from pydantic import BaseModel
from typing import List

class QueryRequest(BaseModel):
    prompt: str
    num_results: int = 5

class QuoteResponse(BaseModel):
    text: str
    author: str

class SimilarQuotesResponse(BaseModel):
    similar_quotes: List[QuoteResponse]
