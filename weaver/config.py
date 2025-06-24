"""
LLM configuration for python-weaver. Users can extend available models as needed.
"""

LLM_CONFIG = {
    # The LLM used to orchestrate high-level planning
    "main_orchestrator": "gpt-4-turbo",

    # Available LLM models for individual tasks
    "available_llms": {
        "gpt-4o-mini": {
            "model": "openai/gpt-4o-mini",
            # Additional litellm params (api_key, max_tokens, etc.) can be provided here
        },
        "gemini-1.5-pro": {
            "model": "gemini/gemini-1.5-pro",
            # Additional parameters...
        },
    }
}
