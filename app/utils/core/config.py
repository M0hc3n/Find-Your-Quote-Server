save_dir = "data/model-dump/quote_model"
input_dir = "data/archive"

llama_config =  {
    "max_new_tokens": 512,
    "prompt_template": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
    "system_prompt": "You are a helpful intellectual assistant who knows a lot of quotes along with their authors."
}