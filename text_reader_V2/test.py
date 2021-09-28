from PIL import Image
import streamlit as st
import pandas as pd
import requests
from DB_class2 import DB_handler as db

# colors hexadecimals
# pink = #F09AE5

    
st.set_page_config(layout="wide")

def preview_candidate(candidate_name, candidate_cv, column):
    column.write("""## Candidate  -  """ + candidate_name)
    column.write("""#### Document""")
    column.write(candidate_cv)

def landing_page_header():
    st.markdown("<h1 style='text-align: center; color: #F09AE5;'> \
                We make your job as a manager much easier!</h1>",
                unsafe_allow_html=True)

    column_1, column_2, column_3 = st.columns(3)
    column_2.markdown("<h5> \
                Are you tired of reading thousands of CV's \
                every day and still not find a person you \
                need for your company? Don't worry! \n Text Reader is here to help you \
                during the hiring process of your company!</h5>",
                unsafe_allow_html=True)

    # Background image(quality is very bad we should change the image later!)

    st.markdown("<h4 style='text-align: center; color: #F09AE5;'> \
                _____________________________________________________________</h4>",
                unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center; color: #F09AE5;'> \
                This is how we helped Tesla hire their favourite data scientists team!</h3>",
                unsafe_allow_html=True)
    column_1, column_2 = st.columns(2)

    image = Image.open("I'm tired CV.jpg")
    column_2.image(image, caption="I'm done with this!", width = 400)
    # ------------------------------------Statistics of how much time you can save----------------------------------------------
    # get Data 
    df = pd.read_csv('hiring.csv')
    # set a subheader
    # show the data as a table
    column_1.dataframe(df)
    my_data = df[['experience', 'interview_score(out of 10)']]
    st.line_chart(my_data)
    st.markdown("<h3 style='text-align: center; color: #F09AE5;'> \
                Consider that experience is not always the most important fact! \
                Don't worry! Text Reader is here to help you during the hiring process of your company!</h3>",
                unsafe_allow_html=True)



    st.markdown("<h4 style='text-align: center; color: #F09AE5;'> \
                _____________________________________________________________</h4>",
                unsafe_allow_html=True)
    # ------------------------------------Statistics of how much time you can save----------------------------------------------

def ml_question_form(candidate_name, candidate_cv, column):
    with column.form("Question form"):
        user_question       = st.text_input(""" Write an important question that you want to know about this candidates CV: """)
        submit_question     = st.form_submit_button("Submit")
        
        if submit_question:
            model_response  = my_module(candidate_cv, user_question)

            candidate_id = db(candidate_name).get_candidate_id()
            db(candidate_name).add_response(candidate_id, user_question, model_response["answer"])
            st.write("Your answer is :", model_response["answer"])
            st.write("Score of the right answer :", model_response["score"])
            
    candidate_id = db(candidate_name).get_candidate_id()
    column.write(db(candidate_name).read_ml_response(candidate_id))

def candidate_db_selectionbox():
    list_of_candidates = db.list_of_candidates()
    selected_candidate  = st.sidebar.selectbox('Candidates Database', list_of_candidates)
    return selected_candidate

def my_streamlit():
    """this function runs the app"""
    # ---------------------------------Streamlit form for adding new candidate cv to database-----------------------------------
    st.sidebar.title("""New candidate""")
    with st.sidebar.form("Upload candidate form"):
        candidate_name  = st.text_input("""Enter candidate name : """).capitalize()
        candidate_cv    = st.text_area("""Paste a copy of CV or cover letter""")
    # Submitbutton
        upload          = st.form_submit_button("Upload")


    # creating list of candidate names names from database candidates.db
    selected_candidate = candidate_db_selectionbox()

    # column layout
    column_1, column_2 = st.columns(2)

    if upload:
        db(candidate_name, candidate_cv).add_candidate()
        preview_candidate(candidate_name, candidate_cv, column_1)
        ml_question_form(candidate_name, candidate_cv, column_2)

    elif selected_candidate:
        candidate_cv =  db(selected_candidate).read_candidate_cv()
        preview_candidate(selected_candidate, candidate_cv, column_1)
        ml_question_form(selected_candidate, candidate_cv, column_2)

    
def my_module(cv, user_question):
    #this function gets cv and user_question and send them to our module
    
    r           = requests.post('http://localhost:8000/start', json = {'name' : 'question_answering'})
    
    url         = "http://localhost:8000/qa"
    body        = {"context": cv , "question":user_question}
    response    = requests.post(url, json=body)
    return response.json()

def main():

    landing_page_header()
    my_streamlit()


    
    

if __name__ == "__main__":
    
    main()