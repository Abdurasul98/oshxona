from datetime import datetime

from core.file_manager import FileManager
from core.utils import get_next_id

def time_dec(func):
    def wrapper(*args, **kwargs):
        time_now = datetime.now()
        hour = time_now.hour
        if hour < 20:
            print("Zakaz berishingiz mumkin")
            return func(*args, **kwargs)
        else:
            print("Abet vaqti tugadi, zakaz qabul qilinmaydi")
            return None
    return wrapper

@time_dec
def add_orders():
    product_id = get_next_id(filename="orders")
    full_name = input("Enter full name: ")
    product_name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    phone = input("Enter phone number: ")
    created_at = datetime.now()

    FileManager("orders").append(row=[product_id, full_name, product_name, quantity, phone, created_at])
    print("New order is added")


def show_product():
    products = FileManager("products").read()
    for product in products:
        print(product)