import sqlite3

# Database for login system
connect = sqlite3.connect('login_app.db')
cursor = connect.cursor()

cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    '''
)
connect.commit()

# هتضيف في التيبول بتاع بيانات التطبيق ال user_id \\ وهتحطه في كل الفانكشنز وفي ال ماين فانكشن هتساويه باللوجن علشان يظبط ومش يجيب ايرورز
def create_account(username, password):
    try:
        cursor.execute('''
            INSERT INTO users(username, password) VALUES(?, ?) 
        ''', (username, password))
        connect.commit()
        print("Account created successfully.")
    except sqlite3.IntegrityError:
        print("This username is already taken. Please choose another one.")

def login(username, password):
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    if user:
        print(f"Welcome, {username}!")
        return user[0]  # Return user ID
    else:
        print("Invalid username or password.")
        return None


def main():
    while True:
        print("-----------------------------LOGIN PAGE-----------------------------------")
        is_user = input("Do you have an account? (Y/N): ")

        if is_user.lower() == 'y':
            username = input("Enter your Username: ")
            password = input("Enter your Password: ")
            user_id = login(username, password)
            if not user_id:
                return
            break

        elif is_user.lower() == 'n':
            create = input("Do you want to create a New Account? (Y/N): ")

            if create.lower() == "y":
                username = input("Enter a username: ")
                password = input("Enter a password: ")
                create_account(username, password)
                user_id = login(username, password)
                if not user_id:
                    return
                break
            else:
                print("You are welcome!")
                return

        else:
            print("Invalid choice, try again!")
            continue


    
# Running code
if __name__ == '__main__':
    main()

connect.commit()
cursor.close()
connect.close()
