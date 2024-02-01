from database import db_connection
import hashlib


def user_creation(user):
    conn, cursor = db_connection()
    cursor.execute(
        "INSERT INTO users (name, type, password) VALUES (?, ?, ?)", (user.name, user.type, '')
    )
    conn.commit()
    id = cursor.lastrowid

    cursor.execute(
        "SELECT * FROM users WHERE id = ?", (id, )
    )
    user_created = cursor.fetchone()
    conn.commit()
    hash_object = hashlib.sha1(str(user_created[0]).encode('utf-8') + str(user_created[1]).encode('utf-8'))
    token = {"id": id, "password": hash_object.hexdigest()}
    cursor.execute(
        "UPDATE users SET password = ? WHERE id = ?",
        (token["password"], token["id"])
    )
    conn.commit()

    return token

def list_users():
    conn, cursor = db_connection()
    cursor.execute(
        "SELECT * FROM users;"
    )
    users = cursor.fetchall()
    return users

if __name__=="__main__":
    print(list_users())