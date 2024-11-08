import replicate

from utils.core.config import llama_config

def call_llama(prompt: str):
    
    input = {**llama_config, 'prompt': prompt}
    
    output = replicate.run(
        "meta/meta-llama-3-8b-instruct",
        input=input
    )
    
    return ''.join(output)