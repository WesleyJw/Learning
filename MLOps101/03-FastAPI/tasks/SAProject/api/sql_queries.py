from database import db_connection
import hashlib

# generate random Gaussian values
from random import seed
from random import gauss
seed(32)



def user_creation(user):
    
    # Set a random number to be used in token generator
    token_seed = str(gauss(2, 3)).encode("utf-8")
    
    # Insert user name and type
    conn, cursor = db_connection()
                                                                      
    cursor.execute(
        "INSERT INTO users (name, type, password) VALUES (?, ?, ?)", (user.name, user.type, '')
    )
    conn.commit()
    
    # get id_user
    id = cursor.lastrowid

    cursor.execute(
        "SELECT * FROM users WHERE id = ?", (id, )
    )
    user_created = cursor.fetchone()
    conn.commit()
    hash_object = hashlib.sha1(str(user_created[0]).encode('utf-8') + str(user_created[1]).encode('utf-8') + token_seed)
    token = {"id": id, "password": hash_object.hexdigest()}
    cursor.execute(
        "UPDATE users SET password = ? WHERE id = ?",
        (token["password"], token["id"])
    )
    conn.commit()
    conn.close()
    return token

def list_users():
    conn, cursor = db_connection()
    cursor.execute(
        "SELECT * FROM users;"
    )
    users = cursor.fetchall()
    conn.close()
    return users

def get_user(password):
    conn, cursor = db_connection()
    cursor.execute(
        "SELECT * FROM users WHERE password = ?;", (password, )
    )
    user = cursor.fetchone()
    conn.close()
    return user

def delete_user(id_user):
    conn, cursor = db_connection()
    cursor.execute(
        "DELETE FROM users WHERE id = ?;", (id_user,)
    )
    conn.commit()
    conn.close()

def history_insert(id_user, text, predict, score):
    conn, cursor = db_connection()
    cursor.execute(
        "INSERT INTO history (id_user, input_text, prediction, score) VALUES (?, ?, ?, ?)", (id_user, text, predict, score)
    )
    conn.commit()
    conn.close()

def get_history(id_user):
    conn, cursor = db_connection()
    cursor.execute(
        "SELECT * FROM history WHERE id_user = ?;", (id_user, )
    )
    history = cursor.fetchall()
    conn.close()
    return history

if __name__=="__main__":
    #delete_user(id_user=3)
    print(get_history(1))
    