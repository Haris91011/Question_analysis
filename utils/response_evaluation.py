from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os

load_dotenv()

output_parser = StrOutputParser()
# openai_key = st.secrets["OPENAI_API_KEY"]
# openai_model = st.secrets["OPENAI_MODEL"]

# # Set the environment variables (optional, if needed elsewhere)
# os.environ["OPENAI_API_KEY"] = openai_key
# os.environ["OPENAI_MODEL"] = openai_model

# # Initialize the OpenAI LLM
# llm = ChatOpenAI(model=openai_model, temperature=0)


openai_key=os.getenv("OPENAI_API_KEY")
llm=ChatOpenAI(model=os.getenv("OPENAI_MODEL"),temperature=0)

def get_evaluation_score(questions,responses):

    prompt = '''Based on the provided question and answer, assign a score between 0 and 10 (inclusive). Only provide the score as an float, without any explanations or additional text.

            Question:
            {question}

            Answer:
            {answer}

            '''
    prompt=ChatPromptTemplate.from_template(prompt)

    chain=llm | output_parser
    
    batch=[]
    for question,answer in zip(questions,responses):
        answer=prompt.invoke({"question":question,"answer":answer})
        batch.append(answer)
    scores=chain.batch(batch)

    for i in range(len(scores)):
        scores[i]=float(scores[i])

    avg_score = sum(scores) / len(scores)
    
    return avg_score