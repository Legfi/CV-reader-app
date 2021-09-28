# ---- Imports ----

import sqlite3

sqlite3.connect('candidates.db').cursor().execute("""CREATE TABLE IF NOT EXISTS candidates_cv(
                name str, 
                cv str
                )""")

# Db handler create and connect to db 
class DB_handler:
    """This class is a set of CRUD methods"""
    def __init__(self, name, cv = 'none'):
        self.name = name
        self.cv = cv
        self.conn = sqlite3.connect('candidates.db')
        self.cursor = self.conn.cursor()

    # CRUD Methods
    # Create
    def add_candidate(self):
        with self.conn:
            self.cursor.execute("INSERT INTO candidates_cv VALUES (:name, :cv)", {'name': self.name, 'cv': self.cv})
            self.conn.commit()

    # Read 
    def read_candidate_cv(self):
        cv = self.conn.execute("SELECT cv FROM candidates_cv WHERE name=:name", {'name': self.name}).fetchone()
        return cv

    # Update 
    def update_cv(self):
        with self.conn:
            self.cursor.execute("""UPDATE candidates_cv SET cv = :cv WHERE name = :name""", 
                            {'name': self.name, 'cv': self.cv})

    # Delete 
    def delete_candidate(self):
        with self.conn:
            self.cursor.execute("DELETE from candidates_cv WHERE name = :name",
            {'name': self.name})
    
    # Creates list of all candidates in database for options in selectionbox 
    @staticmethod
    def list_of_candidates():
        cursor = sqlite3.connect('candidates.db').cursor()
        cursor.execute("SELECT name FROM candidates_cv")
        names = cursor.fetchall()
        list_of_candidates  = []
        for row in names:
            list_of_candidates.append(row[0])
        return list_of_candidates