import sqlite3

username = input('Enter username: ')
password = input('Enter password: ')

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute("""SELECT * FROM users WHERE name = '""")
conn.commit()
print(passwordpython)
