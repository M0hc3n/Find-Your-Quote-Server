import replicate

from utils.core.config import llama_config

def call_llama(prompt: str):
    
    input = {**llama_config, 'prompt': f"I want you to find a quote which best express this feeling or this half-remembered quote: {prompt}. I want you to give me the quote, its author, and in what book he said it, in a JSON style. Return Only the JSON output, with no extra information"}
    
    output = replicate.run(
        "meta/meta-llama-3-8b-instruct",
        input=input
    )
    
    return ''.join(output)