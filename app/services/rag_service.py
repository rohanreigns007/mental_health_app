from transformers import pipeline

# Load your chosen model
rag_pipeline = pipeline("text2text-generation", model="facebook/rag-token-base")

def generate_response(prompt: str) -> str:
    results = rag_pipeline(prompt, max_length=200, num_return_sequences=1)
    return results[0]['generated_text']
