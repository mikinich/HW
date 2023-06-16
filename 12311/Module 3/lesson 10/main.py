import sqlite3
# try:
#     connection = sqlite3.connect('sqlite.db')
# except sqlite3.DatabaseError:
#     print('Ошибка при подключении к БД')
# finally: connection.close()
class User:
    def __init__(self,name: str, surname: str, age: int,gender: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

def get_user(cur: sqlite3.Cursor, gender: int):
    command = '''
    SELECT * FROM employees WHERE gender = ?
    '''
    result = cur.execute(command, (gender,))
    return result.fetchall()

def Delete_users(cur:sqlite3.Cursor):
    command = '''
    DELETE FROM users
    '''
    cur.execute(command)


def get_all_users(cur: sqlite3.Cursor):
    command = '''
    SELECT * FROM users
    '''
    result = cur.execute(command,)
    return result.fetchall()

def update_username(cur:sqlite3.Cursor,  name:str, user_id:int):
    command = '''
    UPDATE users SET name = ? WHERE id = ? 
    '''
    cur.execute(command, (name, user_id))
def add_new_user(cur:sqlite3.Cursor, user: User):
    command = '''
    INSERT INTO users (name, surname, age, gender) VALUES (?, ?, ?, ?) 
    '''
    cur.execute(command, (user.name, user.surname, user.age, user.gender))
def create_user_table(cur: sqlite3.Cursor):
    command = '''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    age INTEGER,
    gender TEXT);
    '''
    cur.execute(command)


if __name__ == '__main__':
    with sqlite3.connect('sqlite.db') as connection:
        cursor = connection.cursor()
        create_user_table(cursor)
        Delete_users(cursor)
        user = User(name='Саня', surname='Атнашев', age=17, gender='male')
        add_new_user(cursor, user=user)

        users = get_user(cursor, 1)
        print(users)
        update_username(cursor, 'Николай', 1)
        print(users)
        users1 = get_all_users(cursor)
        print(users1)