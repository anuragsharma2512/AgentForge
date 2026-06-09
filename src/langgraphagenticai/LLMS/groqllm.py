import os
import streamlit as st

# Attempt to import ChatGroq from langchain_groq. If the package isn't
# installed or import path differs, provide a clear error when the class
# is actually used rather than failing at import time (helps editors/linters).
try:
    from langchain_groq import ChatGroq
except Exception:  # pragma: no cover - fallback for environments without the package
    ChatGroq = None

class GroqLLM:
    def __init__(self, user_contols_input):
        self.user_contols_input = user_contols_input

    def get_llm_model(self):
        try:
            groq_api_key= self.user_contols_input["GROQ_API_KEY"]
            selected_groq_model = self.user_contols_input["selected_groq_model"]
            # Prefer explicit key from UI, fallback to environment variable if not provided
            env_key = os.environ.get("GROQ_API_KEY", "")
            key_to_use = groq_api_key if groq_api_key else env_key

            if not key_to_use:
                st.error("GROQ API key is required. Please set it in the UI or as an environment variable.")
                raise ValueError("GROQ API key is missing")

            if ChatGroq is None:
                raise ImportError("langchain_groq.ChatGroq could not be imported. Install the package or adjust the import path.")

            llm = ChatGroq(api_key=key_to_use, model=selected_groq_model)
        except Exception as e:
            raise ValueError(f"Error initializing GROQ LLM: {e}")
        return llm
        


