from PIL import Image
import streamlit as st
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
    porpose = st.sidebar.selectbox('what is your porpose today?', ['working with a new cv', 'working with an old cv'])
    if porpose == 'working with a new cv':

        #getting user name and greeting
        user_name = st.text_input("""Let's get start! Please Enter your condidate name and press enter button below : """)
        user_name_c = user_name.capitalize()
        if st.button("Enter :)"):
            st.write('Allright! Let see if', user_name_c, 'is your favourit condidate!')

        #here we get the users text and save them as a variable and press submit to use in our model
        with st.form("this is a form"):

            cv = st.text_input("""OK! Just paste a copy of CV or Personal Letter you want to read 
            and leave the rest to us! """)
            user_question = st.text_input(""" Write an important question that you want to know about this CV: """)
            finished = st.form_submit_button("Submit")

            if finished:
                model_response = my_module(cv, user_question)
                st.write("Your answer is :", model_response["answer"])
                st.write("Score of the right answer :", model_response["score"])
                #class function here!!!you can write your codes to call functions in your class to save cvs into database
                #here. delete these comments when you are done!!!
                
    elif porpose == 'working with an old cv':
        st.text_input("""enter the condidates name that you want to work with their cv""")
        #class function here!!!you can write your codes to call functions in your class to read cvs from database
        #here. delete these comments when you are done!!!

        ###############after your codes

        #user_question = st.text_input(""" Write an important question that you want to know about this CV: """)
        #finished = st.form_submit_button("Submit")
        #here when user pick to work with old cv we need cv from your class to put in 
        # my_module(class--> cv, user_question) which i dont know how. otherwise if it's hard we just decide
        # that user only can see the cv or questions here and not interact with them which is what we need for
        # our project that only show from data base!
        #if finished:
        #    model_response = my_module(user_question)
        #    st.write(model_response)




def my_module(cv, user_question):
    #this function gets cv and user_question and send them to our module
    
    r = requests.post('http://localhost:8000/start', json={'name' : 'question_answering'})
    
    url = "http://localhost:8000/qa"
    body = {"context": cv , "question":user_question}
    response = requests.post(url, json=body)
    return response.json()


def main():

    my_streamlit()
    #here is function we need to save data in our database! 
    #my_SQL()


if __name__ == "__main__":
    
    main()