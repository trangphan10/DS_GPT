from langchain_openai import ChatOpenAI 
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI

import os
from dotenv import load_dotenv
load_dotenv()
def load_llm(model_name): 
    # Load Large Language Models 
    '''
    Args: 
        model_name: LLM name 
    Raises: 
        ValueError: when users select unexpected model name 
    Returns: 
        trigger chatbot
    '''
    if model_name == 'gpt-3.5-turbo': 
        return ChatOpenAI(
            model = model_name,
            temperature=0.0,
            max_tokens=1000,
            api_key=os.environ['OPENAI_KEY_API']
        )
    elif model_name  == 'gpt-4':
        return ChatOpenAI(
            model = model_name,
            temperature=0.0,
            max_tokens=1000,
            api_key=os.environ['OPENAI_KEY_API']
        )
    elif model_name == 'gemini-pro':
        # generation_config = {
        #     "temperature": 1,
        #     "top_p": 0.95,
        #     "top_k": 40,
        #     "max_output_tokens": 8192,
        #     "response_mime_type": "text/plain",
        # }
        return ChatGoogleGenerativeAI(
        model="gemini-1.5-pro-002",
        temperature=0.0,
        max_tokens=1000,
        api_key=os.environ["GEMINI_KEY_API"]
        )
       
    else: 
        raise ValueError(
            "Unknown models,  Please choose from ['gpt-3.5-turbo','gpt-4']"
        )