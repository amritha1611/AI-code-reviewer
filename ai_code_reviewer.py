import streamlit as st
from openai import OpenAI

f = open('keys/.openai_api_key.txt')
OPENAI_API_KEY = f.read()

client = OpenAI(api_key=OPENAI_API_KEY)



st.title('AI Code Reviewer')

user_input = st.text_area('Enter your python code:')

if st.button("Generate"):
    st.header("Code Review")

    response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages = [
        {
            'role': 'system',
            'content': """You are a code reviewer. When provided with a code    snippet, perform the following tasks:
            1. Analyze the code thoroughly and identify all bugs, issues, or    areas for improvement. List them clearly under the subheader   **Bug Report**.
            2. Provide the corrected version of the code under the subheader    **Fixed Code**. 
            3. Do not include any additional explanations, comments, or     responses outside these two sections.

            Use the following format for your response, separating the  sections with a forward slash (`/`):
            ### Bug Report
            - [List of identified bugs or issues]
            /
            ### Fixed Code
            [Corrected and improved code here]
            """
        },
        {
            'role': 'user',
            'content': user_input
        }
        ]
    )


    # st.text(response.choices[0].message.content.split('/'))
    res = response.choices[0].message.content.split('/')
    bugs = res[0]
    code = res[1]

    st.markdown(bugs)
    st.markdown(code)