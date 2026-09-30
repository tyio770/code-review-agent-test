def get_user(user_id, cursor):
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)
    return cursor.fetchone()



def login(username, password):
    if username == "admin" and password == "123456":
        return True
    return False


def is_admin(role):
    return role == "admin" or role == "superuser"
