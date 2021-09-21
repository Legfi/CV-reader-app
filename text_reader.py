from PIL import Image
import streamlit as st
import numpy as np
import pandas as pd
import requests

def my_streamlit():
    """this function runs the app"""
    #subtitle
    st.write("""
    # We make your job as a manager much easier than before!""")
    #little bit of information about app
    st.write("""
    ## Are you tired of reading thousands of CV's every day and still not find a person you need for your company?""")

    #showing backgroud image(qulity is very bad we shoud change the image later!)
    image = Image.open("I'm tired CV.jpg")
    st.image(image, caption="I'm done with this!", use_column_width=True)

    #get Data 
    df = pd.read_csv('hiring.csv')
    #set a subheader
    st.subheader('Some facts about how much time you can save:')
    #show the data as a table
    my_data = st.dataframe(df)
    #show statistics on the data
    st.write(df.describe())
    #show the data as a chart
    #chart = st.bar_chart(df)
    st.write(""" 
    ### Don't worry! Text Reader is here to help you during the hiring process of your company!""")
    #getting user name and greeting
    text = st.text_input("""Let's get start! Please Enter your name and press enter button below : """)
    text_capitalize = text.capitalize()
    if st.button("Enter :)"):
        st.write('Welcom to Text Readers', text_capitalize, '!')

    #here we get the users text and save them as a variable to use in our model
    cv = st.text_input("""Allright! Just paste a copy of CV or Personal Letter you want to read 
    and leave the rest to us! """)

    user_question = st.text_input(""" Write an important question that you want to know about this CV: """)

#def my_module():
    """this function gets cv and user_question and send them to our module
    """
    #r = requests.post('http://localhost:8000/start', json={'name' : 'question_answering'})
    #url = "http://localhost:8000/qa"
    #body = {"context": cv , "question":user_question}
    #response = requests.post(url, json=body)

if __name__ == "__main__":
    
    my_streamlit()
    #I've tried this in notbook and it works! it's it's awesome!!! I think this function might run our module!
    #my_module():
    

    #here is function we need to save data in our database! 
    #my_SQL()


