from datetime import datetime

from apps.auth.utils import get_random_code, send_mail
from core.file_manager import FileManager
from core.utils import get_next_id

admin_email = "a"
admin_password = "a"


def check_code():
    user_code = input("Code: ")
    codes = FileManager("codes").read()
    email = None
    for code in codes:
        if code[1] == user_code:
            email = code[0]
            break

    if email is None:
        print("Invalid code")
        return check_code()
    else:
        users = FileManager("users").read()
        for index, user in enumerate(users):
            if user[2] == email:
                users[index][4] = True
                FileManager("users").writerows(data=users)
                return True
    return False


def register():
    full_name = input("Enter your full name: ")
    email = input("Enter your email: ")
    password1 = input("Enter your password: ")
    password2 = input("Confirm your password: ")

    while password1 != password2:
        print("Doesnt not match")
        password1 = input("Enter your password: ")
        password2 = input("Confirm your password: ")

    next_id = get_next_id(filename="users")
    data = [next_id, full_name, email, password2, False, False, datetime.now()]
    FileManager("users").append(data)
    random_code = get_random_code(email=email)
    send_mail(receiver_email=email, body=str(random_code))
    return check_code()


def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    if email == admin_email and password == admin_password:
        return "admin"
    users = FileManager("users").read()
    for index, user in enumerate(users):
        if user[2] == email and user[3] == password:
            users[index][-2] = True
            FileManager("users").writerows(data=users)
            return "user"
    print("Invalid username or password")
    return False


def logout():
    users = FileManager("users").read()
    for index, user in enumerate(users):
        users[index][-2] = False
    FileManager("users").writerows(data=users)


def show_all_users():
    users = FileManager("users").read()
    if not users:
        print("No users yet")
        return

    for user in users:
        print(user)