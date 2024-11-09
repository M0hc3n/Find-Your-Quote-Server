from utils.api.api_models import SimilarQuotesResponse
import json_repair

def output_formatter(output: str):
    json_output = json_repair.loads(output)
    
    res = {
        "response": json_output['quote'],
        "author": json_output['author'],
        "category": json_output['book']
    }
    
    return res
            