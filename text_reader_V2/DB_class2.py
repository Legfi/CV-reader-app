import sqlite3

sqlite3.connect('candidates.db').cursor().execute("""CREATE TABLE IF NOT EXISTS candidates_cv(
                candidate_id int,
                name str, 
                cv str
                )""")

# sqlite3.connect('candidates.db').cursor().execute("""CREATE TABLE IF NOT EXISTS candidates(
#                 name str, 
#                 candidate_id int,
#                 candidate_cv,
#                 )""")

sqlite3.connect('candidates.db').cursor().execute("""CREATE TABLE IF NOT EXISTS Q_and_A(
                candidate_id int,
                question str, 
                answer str
                )""")
# DB handler ---------------------------------------------------------------------------------------------------------------
# create and connect to DB 
class DB_handler:
    """This class is a set of CRUD methods"""
    candidate_id = 1

    def __init__(self, name, cv = 'none'):
        self.name = name
        self.cv = cv
        self.conn = sqlite3.connect('candidates.db')
        self.cursor = self.conn.cursor()
        # create database table candidates_cv 

    # ----------------------- CRUD Methods -----------------------
    # Create ---------------
    def add_candidate(self):
        with self.conn:
            self.cursor.execute("INSERT INTO candidates_cv VALUES (:candidate_id, :name, :cv)", 
                                {'candidate_id': DB_handler.candidate_id, 'name': self.name, 'cv': self.cv})
            self.conn.commit()
        DB_handler.candidate_id += 1

    def add_response(self, candidate_id, question, answer):
        with self.conn:
            self.cursor.execute("INSERT INTO Q_and_A VALUES (:candidate_id, :question, :answer)", 
                                {'candidate_id': candidate_id, 'question': question, 'answer': answer})
            self.conn.commit()

    # Read ---------------
    def read_candidate_cv(self):
        cv = self.conn.execute("SELECT cv FROM candidates_cv WHERE name=:name", {'name': self.name}).fetchone()
        return str(cv).replace("('", "").replace("',)", "").replace('("', '').replace('",)', '')
    
    def read_ml_response(self, candidate_id):
        question = self.conn.execute("SELECT question FROM Q_and_A WHERE candidate_id=:candidate_id", {'candidate_id': candidate_id}).fetchall()
        answer = self.conn.execute("SELECT answer FROM Q_and_A WHERE candidate_id=:candidate_id", {'candidate_id': candidate_id}).fetchall()
        cleaned = str(answer).replace("('", "").replace("',)", "").replace('("', '').replace('",)', '')

        list_of_QnA = []
        for i in range(len(question)):
            concatenate = 'QUESTION: ' + str(question[i]).replace("('", "").replace("',)", "").replace('("', '').replace('",)', '') \
                        + ' - ANSWER: ' + str(answer[i]).replace("('", "").replace("',)", "").replace('("', '').replace('",)', '')
            list_of_QnA.append(concatenate)
            # return_string = 'Question: '+ str(question[i]).replace("('", "").replace("',)", "").replace('("', '').replace('",)', '') \
            #                         + '\n' + 'Answer:' + str(answer[i]).replace("('", "").replace("',)", "").replace('("', '').replace('",)', '')
        return list_of_QnA
        
    def get_candidate_id(self):
        candidate_id = self.conn.execute("SELECT candidate_id FROM candidates_cv WHERE name=:name", {'name': self.name}).fetchone()
        return str(candidate_id).replace("(", "").replace(",)", "")

    # Update ---------------
    def update_cv(self):
        with self.conn:
            self.cursor.execute("""UPDATE candidates_cv SET cv = :cv WHERE name = :name""", 
                            {'name': self.name, 'cv': self.cv})

    # Delete ---------------
    def delete_candidate(self):
        with self.conn:
            self.cursor.execute("DELETE from candidates_cv WHERE name = :name",
            {'name': self.name})
    
    @staticmethod
    def list_of_candidates():
        cursor = sqlite3.connect('candidates.db').cursor()
        cursor.execute("SELECT name FROM candidates_cv")
        names = cursor.fetchall()
        list_of_candidates  = []
        for row in names:
            list_of_candidates.append(row[0])
        return list_of_candidates
    # ----------------------- CRUD Methods -----------------------
    # DB handler ---------------------------------------------------------------------------------------------------------------
