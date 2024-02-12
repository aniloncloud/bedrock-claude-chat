# Configure generation parameter for Claude chat response.
# Adjust the values according to your application.
# See: https://docs.anthropic.com/claude/reference/complete_post
GENERATION_CONFIG = {
    "max_tokens_to_sample": 2000,
    "temperature": 0.6,
    "top_k": 250,
    "top_p": 0.999,
    "stop_sequences": ["Human: ", "Assistant: "],
}

# Configure embedding parameter.
EMBEDDING_CONFIG = {
    # DO NOT change `model_id` (currently other models are not supported)
    "model_id": "cohere.embed-multilingual-v3",
    # NOTE: consider that cohere allows up to 2048 tokens per request
    "chunk_size": 1000,
    "chunk_overlap": 200,
}

# Configure search parameter to fetch relevant documents from vector store.
SEARCH_CONFIG = {
    "max_results": 5,
}

# Configure llama2 70B model parameters
LLAMA2_70B_CONFIG = {
    # Add the specific parameters required by the llama2 70B model here
    # For example:
    "model_id": "llama2-70B",
    "max_tokens": 4096,
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 50,
    "frequency_penalty": 0.6,
    "presence_penalty": 0.6,
    "stop_sequences": ["<end of text>"],
}