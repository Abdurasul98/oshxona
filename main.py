def main():
    while True:
        print("""
        1. Register
        2. Login
        3. Logout
        4. exit
        """)
        choice = input("choice: ")

        if choice == "1":
            pass

        elif choice =="2":
            role = ""
            if role == "admin":
                admin()
            elif role == "user":
                user()
            else:
                print("wrong")

        elif choice =="3":
            pass

        elif choice =="4":
            break

        else:
            print("invalid choice")


def admin():
    print("""
    1. Show orders
    2. Delete orders
    3. Show users
    4. Total place
    """)

    choice = input("choice: ")

    if choice == "1":
        pass

    elif choice == "2":
        pass

    elif choice == "3":
        pass

    elif choice == "4":
        pass

    else:
        print("invalid choice")
        return admin()


def user():
    print("""
    1. Add orders
    2. Show orders
    """)

    choice = input("choice: ")

    if choice == "1":
        pass

    elif choice == "2":
        pass

    else:
        print("invalid choice")
        return user()



if __name__ == "__main__":
    main()