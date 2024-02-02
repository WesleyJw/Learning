from database import db_connection

def user_auth(password):
    """User Authentication by password

    Args:
        password (str): A user password
    """
    
    conn, cursor = db_connection()
    cursor.execute(
        "SELECT * FROM users WHERE password = ?", (password,)
    )
    user = cursor.fetchone()
    conn.close()
    return user

def password_auth(name, password):
    """User Authentication by password

    Args:
        password (str): A user password
    """
    
    conn, cursor = db_connection()
    cursor.execute(
        f"SELECT * FROM users WHERE name = {name} AND password = {password}"
    )
    user = cursor.fetchone()
    conn.close()
    return user

def authenticated_user(token):
    user_token = user_auth(password=str(token))
    print(user_token[3])
    if str(token) != user_token[3]:
        print(user_token[3])
    if user_token[2] != "admin":
        print(user_token[3])

if __name__=="__main__":
    print(user_auth(password='123456'))
    authenticated_user('123456')