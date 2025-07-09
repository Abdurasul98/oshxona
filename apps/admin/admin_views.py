from core.file_manager import FileManager
from datetime import datetime
from core.utils import get_next_id


def delete_orders():
    phone_number = input("phone_number: ").strip()
    new_order = []
    lampochka =True

    reader = FileManager("orders").read()
    for i in reader:
        if i[4].strip() != phone_number:
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
    product = input("Product: ")

    while True:
        quantity = int(input("Mahsulot soni: "))
        if quantity > 0:
            break
        else:
            print("Iltimos, musbat son kiriting.")


    order_id = get_next_id("orders")
    order_time = datetime.now()
    data = [order_id,product,quantity,order_time]

    FileManager("orders").append(data)
    print("Added product")

def delete_products():
    order_id = input("order_id")

    file = FileManager("orders")
    orders = file.read()

    new_orders = []
    lampochka = False

    for i in orders:
        if i[0] != order_id:
            new_orders.append(i)
        else:
            lampochka = True


    if lampochka:
        file.writerows(new_orders)
        print("Deleted order")
    else:
        print("Not found this order")