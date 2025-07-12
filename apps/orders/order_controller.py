from core.file_manager import FileManager
from datetime import datetime

def show_orders():
    orders = FileManager("orders").read()
    for order in orders:
        if len(order) < 7 or order[0] == "ID":
            continue
        print(f"ID: {order[0]} Name: {order[1]} Product: {order[2]} Quantity: {order[3]} Phone: {order[4]} Created at: {order[5]} Time: {order[6]}")


order_file = FileManager("orders")
def orders_time(user_id: int, order_time: str):

    datetime.strptime(order_time, "%H:%M")

    file = FileManager("order_time_log")
    data = file.read()

    if not data:
        data = [["user_id","order_time"]]
        file.writerows(data)

    file.append([user_id,order_time])