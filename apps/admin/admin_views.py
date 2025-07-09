from core.file_manager import FileManager


def delete_orders():
    phone_number = input("phone_number: ")
    new_order = []
    lampochka =True
    reader = FileManager("orders").read()
    for i in reader:
        if i[4] != phone_number:
            new_order.append(i)
        else:
            lampochka = False

    if lampochka:
        FileManager("orders").writerows(new_order)
        print("Deleted order")
    else:
        print("Not found order")

def show_users():
    reader = FileManager("users").read()
    for i in reader:
        print(i)


def total_place():
    total = 100
    busy = 0

    reader = FileManager("orders").read()

    for i in reader:
        busy = busy + int(i[3])
    result = total - busy
    print(f"{result}ta bosh joy")


def add_products():
    pass


def delete_products():
    pass