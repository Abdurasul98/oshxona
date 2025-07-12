from datetime import datetime

from core.file_manager import FileManager
from core.utils import get_next_id

from apps.orders.order_controller import orders_time
def add_orders():
    product_id = get_next_id(filename="orders")
    full_name = input("Enter full name: ")
    product_name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    phone = input("Enter phone number: ")
    created_at = datetime.now()
    order_time = input("Enter oreder time for example (HH:MM): ")
    orders_time(user_id=product_id,order_time=order_time)

    FileManager("orders").append(row=[product_id, full_name, product_name, quantity, phone, created_at,order_time])
    print("New order is added")



def show_product():
    pass