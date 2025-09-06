import mysql.connector as sql

def connect():
    return sql.connect(
    host = "localhost",
    user = "root",
    password = "Arif12@1",
    database = "Bank_System"
)

