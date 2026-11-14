
menue = {
    "coffee": 80000,
    "tea": 50000,
    "cake": 120000
}

def show_menue():
    print("====== Cafe Menue ======")

    for product, price in menue.items():
        print(product, ":", price, "Tomans")
