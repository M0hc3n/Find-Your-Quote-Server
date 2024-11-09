from fastapi import FastAPI, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn, aiohttp, asyncio, aiofiles, os
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException

from utils.api.api_models import SimilarQuotesResponse
from model.inference import find_similar_quotes
# from utils.model.load_model import load_model
# from utils.data.load_quotes import load_quotes_from_json

from utils.api.api_models import QueryRequest, QuoteResponse, SimilarQuotesResponse

from utils.model.call_llama import call_llama
from utils.api.llama_output_formatter import output_formatter

from getpass import getpass

# REPLICATE_API_TOKEN = getpass()

# os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN

app = FastAPI()

# vector_db, model = load_model()
# quotes = load_quotes_from_json()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=origins,
    allow_headers=origins,
)

# @app.post("/find-similar-quotes", response_model=SimilarQuotesResponse)
# async def infere_similar_quotes(query: QueryRequest):
#     try:
#         similar_indices = find_similar_quotes(query.prompt, vector_db, model, k=query.num_results)
#         similar_quotes = [QuoteResponse(response=quotes[i]['Quote'], author=quotes[i]['Author'], category=quotes[i]["Category"]) for i in similar_indices]
#         return SimilarQuotesResponse(similar_quotes=similar_quotes)

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/find-similar-quotes-using-llama")
async def infere_similar_quotes(query: QueryRequest, response_model=SimilarQuotesResponse):
    try:
        output = call_llama(query.prompt)
        print(output)
        res = output_formatter(output)
        
        return SimilarQuotesResponse(similar_quotes=[res])
                
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, port=3987)
