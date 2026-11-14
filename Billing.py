
from Order import orders

def calculate_total():
    total = 0

    for order in orders:
        total += order["price"] * order["quantity"]

    return total


def calculate_discount(total):
    if total > 1000000:
        discount = total * 0.10
    else:
        discount = 0

    return discount


def print_invoice():
    if not orders:
        print("No orders to print.")
        return

    print("========== INVOICE ==========")

    for order in orders:
        print(order["product"], "x", order["quantity"])

    total = calculate_total()
    discount = calculate_discount(total)
    final_amount = total - discount

    print("-----------------------------")
    print("Total:", total, "Tomans")
    print("Discount:", discount, "Tomans")
    print("Final payment:", final_amount, "Tomans")
    print("=============================")
