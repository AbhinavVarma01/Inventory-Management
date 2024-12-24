#!C:\Users\abhin\AppData\Local\Programs\Python\Python37\python.exe
import os
import cgi
import cgitb
import sqlite3

cgitb.enable()
print("Content-type: text/html\n\n")
print("<html><body style='text-align:center;'>")
print("<h1 style='color: m ;'>LOGIN PAGE</h1>")
form = cgi.FieldStorage()
name = ""
pwd = ""
if os.environ['REQUEST_METHOD'].upper() == 'POST':
   
    if form.getvalue("username"):
        name = form.getvalue("username")
    if form.getvalue("password"):
        pwd = form.getvalue("password")
    def connect_to_db(db_name):
        try:
            con = sqlite3.connect(db_name)
            return con
        except sqlite3.Error as error:
            print("<p>Error while connecting to SQLite: " + str(error) + "</p>")
            return None
    db_name = "Abhinav1.db"
    con = connect_to_db(db_name)

    if con:
        try:
            cur = con.cursor()
            sql_select = "SELECT * FROM login WHERE username = ? AND password = ?"
            cur.execute(sql_select, (name, pwd))
            rec = cur.fetchone()
            if rec:  
                print('<meta http-equiv="refresh" content="0;url=inventory.html" />')
            else:  
                print("<script>alert('Login failed. Please try again.'); window.location.href = 'login_form.html';</script>")
        except sqlite3.Error as error:
            print("<p>Error while executing SQL query: " + str(error) + "</p>")
        finally:
            con.close()
    else:
        print("<p>Failed to connect to the database</p>")

print("</body></html>")
