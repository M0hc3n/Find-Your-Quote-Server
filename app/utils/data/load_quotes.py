import json

from utils.core.config import input_dir

def load_quotes_from_json():
    file_path = input_dir + "/full_quotes_json.json"
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            quotes = json.load(file)
        print(f"Successfully loaded {len(quotes)} quotes.")
        return quotes
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} is not valid JSON.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return []