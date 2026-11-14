
from Menue import show_menue
from Order import add_order, show_orders
from Billing import calculate_total, print_invoice

while True:
    print("\n========== Coffee Shop ==========")
    print("1. Show Cafe Menu")
    print("2. Add Order")
    print("3. Show Orders")
    print("4. Calculate Total")
    print("5. Print Invoice")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_menue()

    elif choice == "2":
        add_order()

    elif choice == "3":
        show_orders()

    elif choice == "4":
        print("Total:", calculate_total(), "Tomans")

    elif choice == "5":
        print_invoice()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
