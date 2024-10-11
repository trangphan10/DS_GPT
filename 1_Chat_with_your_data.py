import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 
# Read environment files
from dotenv import load_dotenv
# Agents for data science to enhance GPT abilities: 
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
import google.generativeai as genai
from src.logger.base import BaseLogger
from src.models.llm import load_llm
# load env variables 
load_dotenv()
logger = BaseLogger()
MODEL_NAME = 'gemini-pro'

def process_query(da_agent,query): 
    pass

def main(): 
    # thinking about how implement operations in main function 
    # Set up streamlit interface 
    st.set_page_config(
        page_title='Smart Data Analysis Tool',
        layout='centered'
    )
    st.header('Smart Data Analysis Tool')
    st.write('Welcome to our data analysis tool. This tool can assist your daily data analysis task')
    # load LLM model 
    llm = load_llm(model_name=MODEL_NAME)
    logger.info(f'Successfully loaded {MODEL_NAME}')
    # Upload csv file 
    with st.sidebar:
        uploaded_file = st.file_uploader("Upload your csv file here",type='csv')
        
    # Initial chat history
    if 'history' not in st.session_state:
        st.session_state.history = []
    # Read csv file 
    if uploaded_file is not None: 
        st.session_state.df = pd.read_csv(uploaded_file)
        # Check whether file is uploaded successfully 
        st.write('### Your uploaded data:',st.session_state.df.head(10))
    
    # Create data analysis agent to query with our data
    da_agent = create_pandas_dataframe_agent(
        llm=llm,
        df=st.session_state.df,
        agent_type='tool-calling',
        # Allow Python run code
        allow_dangerous_code=True,
        # display LLM agent response 
        verbose=True,
        return_intermediate_steps=True,
    )
    logger.info('### Successfully loaded data analysis agent| ###')
    # Input query and process query
    query = st.text_input('Enter your question:')
    if st.button('Run query'): 
        with st.spinner('Processing...'): 
            process_query(da_agent,query)
    pass 

if __name__ =='__main__': 
    main()
