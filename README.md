#  A Very Simple Machine Learning Application: A Group Project.
## Brief Summary: 

We use a Machine Learning module that we access via an API (Application Programming Interface) request. We also make use of the Streamlit library. The idea at large was that the user uploads data into a database and the user can then reach the saved information that is sorted under the name of the applicant. The simple database used is SQLite. The applicants data can then be used in order to answer very simple questions that are connected to the text copied into the Streamlit. For example, what if HR (Human Resources) wanted to easily access different data and not have to read through all of the text that the candidate provided within a textfile. HR is then able to ask questions and the Machine Learning API provides an answer and a probability. 

## Build Status:

Completed. 

No bugs or errors in need of addressing. We hope.

## Code Style:

Standard. The code follows coding conventions for Python by using PEP8 framework. 

## Tech/Framework used:

Streamlit, Pandas, Sqlite3. 

## Features: 

The application can search through a textfile and with machine learning answer some questions. We used it in a HR situation but the API can answer more   

## Code Example:

This is an example of the function that runs the app: 

def my_streamlit():

    # application pitch
    st.write("""# We make your job as a manager much easier than before!""")
    st.write("""## Are you tired of reading thousands of CV's every day and still not find a person you need for your company?""")

    # background image
    image = Image.open("I'm tired CV.jpg")
    st.image(image, caption="I'm done with this!", use_column_width=True)

    # statistics on how much time you can save
    # gets data 
    df = pd.read_csv('hiring.csv')
    # sets a subheader
    st.subheader('This is how we helped Tesla hire their favourite data scientists team:')
    # shows the data as a table
    st.dataframe(df)
    my_data = df[['experience', 'interview_score(out of 10)']]
    st.line_chart(my_data)
    st.write("""### Consider that experience is not always the most important fact!""")
    st.write("""### Don't worry! Text Reader is here to help you during the hiring process of your company!""")

The code should look something like this in your visual studio code:

<img width="1055" alt="Screenshot_1" src="https://user-images.githubusercontent.com/89390286/134901180-820946d8-c074-49ca-8795-30acf40267fb.png">

## Installation:

You need to import the following modules into python: Streamlit, Pandas, and Sqlit3. This is a guide on how to import modules into python. 

https://www.geeksforgeeks.org/import-module-python/

## API reference:

Not available at the moment. 

## Tests:

This is the section where you mention all the different tests that can be performed with code examples

## User-guide:

1. Open the python file text_reader.py. 

2. Enter this in terminal: streamlit run text_reader.py 

3. Default is to add a new candidate then enter name. Enter CV in textform and then press upload. The select box should be looking like the select box below: 

<img width="1668" alt="Screenshot_2" src="https://user-images.githubusercontent.com/89390286/134902383-3b712bb7-c8cf-4dde-9772-a71e0390d21e.png">

4. If you have done this in a previous session or just some time ago and want to review the candidate information and ask questions then the select box should be looking like the one below instead:

<img width="1676" alt="Screenshot_3" src="https://user-images.githubusercontent.com/89390286/134902607-f72e8215-a82b-4d1c-ae0b-dc722dc82453.png">

 
## Contribute:

If you want to contribute to the code and this project it is made possible by commiting new code to github.


