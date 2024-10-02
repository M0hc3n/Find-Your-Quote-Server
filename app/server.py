from fastapi import FastAPI, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import asyncio
import aiohttp
import aiofiles
from fastapi.middleware.cors import CORSMiddleware

from app.utils.api.api_models import SimilarQuotesResponse
from app.model.inference import find_similar_quotes
from app.utils.model.load_model import load_model
from app.utils.data.load_quotes import load_quotes_from_json

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

vector_db, model = load_model()
quotes = load_quotes_from_json()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/find-similar-quotes", response_model=SimilarQuotesResponse)
async def find_similar_quotes(query: QueryRequest):
    try:
        similar_indices = find_similar_quotes(query.prompt, vector_db, model, k=query.num_results)
        similar_quotes = [QuoteResponse(text=quotes[i]['Quote'], author=quotes[i]['Author']) for i in similar_indices]
        return SimilarQuotesResponse(similar_quotes=similar_quotes)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3987)
