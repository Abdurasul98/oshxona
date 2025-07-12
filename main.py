from apps.admin.admin_views import delete_orders, show_users, total_place, add_products, delete_products, show_products
from apps.auth.views import register, login, logout
from apps.orders.order_controller import show_orders
from apps.user.user_views import add_orders


def main():
    print("""
        1. Register
        2. Login
        3. Exit
        """)

    choice = input("choice: ")

    if choice == "1":
        register()
    elif choice =="2":
        role = login()
        if role == "admin":
            admin()
        elif role == "user":
            user()
        else:
            print("wrong")
    elif choice =="3":
        return main()
    else:
        print("invalid choice")


def admin():
    print("""
        1. Show orders
        2. Delete orders   
        3. Show users
        4. Total place
        5. Add products
        6. Show products
        7. Delete products
        8. Logout
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
        add_products()
    elif choice == "6":
        show_products()
    elif choice == "7":
        delete_products()
    elif choice == "8":
        logout()
        return main()
    else:
        print("invalid choice")
    return admin()



def user():
    print("""
    1. Add orders
    2. Show orders
    3. Show product
    4. Logout
    """)

    choice = input("choice: ")

    if choice == "1":
        add_orders()
    elif choice == "2":
        show_orders()
    elif choice == "3":
        show_products()
    elif choice == "4":
        logout()
        return main()
    else:
        print("invalid choice")
    return user()



if __name__ == "__main__":
    main()