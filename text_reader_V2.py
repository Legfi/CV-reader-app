# ---- Imports ----

from typing import Text
from PIL import Image
import streamlit as st
import pandas as pd
import requests
import time
from DB_class import DB_handler as db


# ---- Functions ----

def my_streamlit():
    """This function runs the app"""
    #adding music
    audio_file = open('music.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, start_time=0)
    # Application pitch
    st.write("""# We make your job as a manager much easier than before!""")
    st.write("""## Are you tired of reading thousands of CV's every day and still not find a person you need for your company?""")

    # Background image
    image = Image.open("I'm tired CV.jpg")
    st.image(image, caption="I'm done with this!", use_column_width=True)

    # Statistics on how much time you can save
    # Gets data 
    df = pd.read_csv('hiring.csv')
    # Sets a subheader
    st.subheader('This is how we helped Tesla hire their favourite data scientists team:')
    # Shows the data as a table
    st.dataframe(df)
    my_data = df[['experience', 'interview_score(out of 10)']]
    st.line_chart(my_data)
    st.write("""### Consider that experience is not always the most important fact!""")
    st.write("""### Don't worry! Text Reader is here to help you during the hiring process of your company!""")

def decision():
    # Multiple choice selectionbox
    purpose = st.selectbox(
        'Would you like to add new candidate, or review existing candidates in database', 
        ['Add new candidate', 'Review existing candidates'])

    # Streamlit form for adding new candidate cv to database
    if purpose == 'Add new candidate':
        st.write("""Enter name and paste cv or personal letter and press the upload button to add new candidate""")
        
        with st.form("Upload candidate form"):
            candidate_name  = st.text_input("""Enter candidate name : """).capitalize()
            candidate_cv    = st.text_input("""Paste a copy of CV or Personal Letter""")
        
    # Submit button
            upload          = st.form_submit_button("Upload")
            if upload:
    # Database create function
                db(candidate_name, candidate_cv).add_candidate()
    #This is a code that acceptes multiple files            
        uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            st.write("filename:", uploaded_file.name)
            st.write(bytes_data)

    # Streamlit form for submitting question to ML-model
    elif purpose == 'Review existing candidates':

        st.write("""First select a candidate in the dropdown menu, then type in a question and press submit to get your answer""")

    # Creating list of candidate names names from database candidates.db
        list_of_candidates = db.list_of_candidates()
    #starting the QA model
        requests.post('http://localhost:8000/start', json = {'name' : 'question_answering'})
    
    # Question form and candidate selection box
        with st.form("Question form1"):
            selected_candidate  = st.selectbox('Candidates', list_of_candidates)
            candidate_cv        = str(db(selected_candidate).read_candidate_cv())
            user_question       = st.text_input(""" You can always write your question 
            directly here! otherwise just submit and leave the rest to us : """)
            submit_question     = st.form_submit_button("Submit")
            
            if submit_question:
                with st.spinner('Wait for it...'):
                    time.sleep(10)
    #these reurns answer from our functions that interact with our models    
                model_response1  = my_module(candidate_cv)
                model_response2 = my_module2(candidate_cv)
                model_response3 = my_module2(candidate_cv)
                model_response4 = my_module4(candidate_cv, user_question)
    #showing answers a bit clear by getting them from our json files
                st.write("Age:", model_response1["answer"])
                st.write("Score of the right answer :", model_response1["score"])
                st.write("Experiens:", model_response2["answer"])
                st.write("Score of the right answer :", model_response2["score"])
                st.write("Education:", model_response3["answer"])
                st.write("Score of the right answer :", model_response3["score"])
                st.write("Answer:", model_response4["answer"])
                st.write("Score of the right answer :", model_response4["score"])
                st.balloons()
def my_module(cv):
    """This function selects cv and user_question returns to module"""    
    url         = "http://localhost:8000/qa"
    body1        = {"context": cv , "question":"How old is he?"}
    response1    = requests.post(url, json=body1)
    return response1.json() 
    
def my_module2(cv):
    """This function selects cv and user_question returns to module"""    
    url         = "http://localhost:8000/qa"
    body       = {"context": cv , "question":"How much experience?"}
    response2    = requests.post(url, json=body)
    return response2.json()


def my_module3(cv):
    """This function selects cv and user_question returns to module"""    
    url         = "http://localhost:8000/qa"
    body        = {"context": cv , "question":"what does he/she studied?"}
    response3    = requests.post(url, json=body)
    return response3.json()


def my_module4(cv, user_question):
    """This function selects cv and user_question returns to module""" 
    user_question = '?'
    url         = "http://localhost:8000/qa"
    body        = {"context": cv , "question": user_question}
    response4    = requests.post(url, json=body)
    return response4.json()


def main():
    """When running this script this is the main module that handles the appplications logic"""
    my_streamlit()
    decision()

# ---- Mainmethod ----

if __name__ == "__main__":
    main()