from apps.admin.admin_views import  delete_orders, show_users, total_place
from apps.auth.views import register, login, logout
from apps.orders.order_controller import show_orders
from apps.user.user_views import add_orders


def auth_menu():
    print("""
    1. Register
    2. Login
    3. Exit
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        if register():
            print("Successfully registered")
        else:
            print("Something went wrong")
    elif choice == "2":
        result = login()
        if result == "admin":
            print("Welcome admin")
            return admin_menu()
        elif result == "user":
            print("Welcome user")
            return user_menu()
        else:
            return login()
    elif choice == "3":
        print("Good bye")
        return
    else:
        print("Invalid choice")
    return auth_menu()


def admin_menu():
    print("""
    1. Show orders
    2. Delete orders
    3. Show users
    4. Total place
    5. Logout
    """)

    choice = input("choice: ")

    if choice == "1":
        show_orders()

    elif choice == "2":
        delete_orders()

    elif choice == "3":
        show_users()

    elif choice == "4":
        total_place()

    elif choice == "5":
        logout()
        return auth_menu()

    else:
        print("invalid choice")
    return admin_menu()


def user_menu():
    print("""
    1. Add orders
    2. Show orders
    3. Logout
    """)

    choice = input("choice: ")

    if choice == "1":
        add_orders()

    elif choice == "2":
        show_orders()

    elif choice == "3":
        logout()
        return auth_menu()

    else:
        print("invalid choice")
    return user_menu()



if __name__ == "__main__":
    auth_menu()