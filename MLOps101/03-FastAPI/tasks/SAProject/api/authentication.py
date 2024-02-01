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

if __name__=="__main__":
    print(user_auth(name='Wesley')[1])