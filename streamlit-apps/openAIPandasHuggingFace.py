"""
streamlit run openAIPandasHuggingFace.py --server.enableCORS=false
"""

import openai
import streamlit as st
from datasets import load_dataset

st.title("The Squad")

"""
squad_dataset = load_dataset('squad')
print(squad_dataset['train'][0])
"""

from datasets import load_dataset
import openai
import os

def submit_question(text):
    """This submits a question to the OpenAI API"""

    openai.api_key = os.getenv("OPENAI_API_KEY")

    return openai.Completion.create(
        prompt=text,
        temperature=0,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        model="text-davinci-002",
    )["choices"][0]["text"].strip(" \n")


def squad_dataset():
    return load_dataset("squad")

@st.cache
def load_data(row):
    dataset = squad_dataset()
    payload = squad_dataset()['train'][row]['context']
    return submit_question(payload)

data_load_state = st.text('Loading data and giving to openai...')
data = load_data(0)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)