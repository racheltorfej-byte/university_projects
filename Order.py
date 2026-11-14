
from Menue import menue

orders = []

def add_order():
    product = input("Enter product name: ").lower()

    if product not in menue:
        print("Product not found!")
        return

    quantity = int(input("Enter quantity: "))

    order = {
        "product": product,
        "price": menue[product],
        "quantity": quantity
    }

    orders.append(order)

    print("Order added successfully!")


def show_orders():
    if not orders:
        print("No orders have been registered.")
        return

    for order in orders:
        print("Product:", order["product"])
        print("Price:", order["price"])
        print("Quantity:", order["quantity"])
        print("----------------")
