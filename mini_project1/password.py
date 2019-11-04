import sys
import hashlib
import re


connection = None
cursor = None
conn = sqlite3.connect('./test.db')
c = conn.cursor()

username = input("Please input uid: ")
password = input("Please input password: ")
if re.match("^[A-Za-z0-9_]*$", username) and re.match("^[A-Za-z0-9_]*$", password):
    encrypt(password)
    conn.create_function("hash", 1, encrypt)
    data = (username, password)
    c.execute(" INSERT INTO users (uid, pwd) VALUES (?, hash(?)) ", data )
    data = (password, )
    uid = c.execute(" SELECT uid FROM member WHERE pedd LIKE hash(?) ", data).fetchall()
    user_uid = c.execute('SELECT * FROM users WHERE uid=?;' , (uid,)).fetchall()
    if username != user_uid:
        raise Exception('Invalid uid or password.')
def encrypt(password):
    alg = hashlib.sha256()
    alg.update(password.encode("utf-8"))
    return alg.hexdigest()





