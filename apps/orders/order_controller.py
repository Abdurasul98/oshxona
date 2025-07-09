from core.file_manager import FileManager


def show_orders():
    orders = FileManager("orders").read()
    for order in orders:
        print(f"ID: {order[0]} Name: {order[1]} Product: {order[2]} Quantity: {order[3]} Phone: {order[4]} Created at: {order[5]}")

