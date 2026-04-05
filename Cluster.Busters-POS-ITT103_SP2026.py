#Point of Sale (POS) system program for Best Buy Retail Store

#Store items catalog
store_catalog = {
    'soda':    {'price': 120, 'stock': 150},
    'bread':   {'price': 425, 'stock': 100},
    'water':   {'price': 100,  'stock': 300},
    'cheese':  {'price': 50,  'stock': 150},
    'bun':     {'price': 80,  'stock': 200},
    'soap':    {'price': 150, 'stock': 400},
    'sugar':   {'price': 50,  'stock': 120},
    'milo':  {'price': 120, 'stock': 200},
    'lasco': {'price': 120,  'stock': 200},
    'crackers':{'price': 75,  'stock': 300},
}
#Dictionary for low stock warnings
low_stock ={}

#Customer checkout cart dictionary
checkout_list = {}

#Default function for displaying store catalog
def show_store():
    print('~~~~~~~~~~~~List of available items and prices~~~~~~~~~~~~')
    for name, info in store_catalog.items():
        low_warning = " LOW STOCK" if info['stock'] < 5 else""
        print(f" {name}: ${info['price']} x {info['stock']}{low_warning} ")


    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ('')


#Calculations/formulas~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Default function for adding items to cart
def add_to_checkout():
    name= input("Please select a store item you would like to add(press 'x' to return): ").strip().lower()
    if name == 'x':
        return
    elif name not in store_catalog:
        print("Invalid item.")
        return
    qty = int(input("Enter the amount you would like to purchase: "))
    if qty <= 0 or qty > store_catalog[name]['stock']:
        print("Invalid amount.")
        return
    current_in_cart = checkout_list.get(name, 0)
    store_catalog[name]['stock'] -= qty
    checkout_list[name] = current_in_cart + qty
    print(f"{qty} x {name} have been added to your cart.")
    if store_catalog[name]['stock'] < 5:
        print(f"Warning {store_catalog[name]['stock']} stock left.")
        low_stock[name] = store_catalog[name]['stock']

#Default function for removing an item from the cart
def remove_from_checkout():
    name = input("Please select a cart item you would like to remove(press 'x' to return): ").strip().lower()
    if name == 'x':
        return
    elif name not in checkout_list:
        print("This item is not in your cart.")
        return
    qty = int(input("Enter the amount you would like to remove: "))
    if qty <= 0:
        print("Invalid amount.")
        return
    in_cart = checkout_list[name]
    if qty >= in_cart:
        qty_returned = in_cart
        del checkout_list[name]
        print(f"{qty_returned} x {name} have been removed from your cart.")
    else:
        checkout_list[name] = in_cart - qty
        qty_returned = qty
        print(f"{qty} x {name} have been removed from your cart.")
    store_catalog[name]['stock'] += qty_returned
    if store_catalog[name]['stock'] >= 5 and name in low_stock:
        del low_stock[name]

#Default function for displaying selected items
def show_cart():
    if not checkout_list:
        print("There are no items in your cart.")
        return
    total = 0
    for name, qty in checkout_list.items():
        price = store_catalog[name]['price']
        unit_total = price * qty
        total += unit_total
        print(f" {name}: qty {qty}, unit price ${price}, ${unit_total}")
    print(" ")


#Default function for finalizing checkout
def checkout():
    if not checkout_list:
        print("There are no items in your cart.")
        return
    show_cart()
    final_checkout = input("Are you sure you would like to check out your cart? (Press 'Y' to confirm): ").strip().lower()
    if final_checkout == 'y':
        total = sum(store_catalog[name]['price'] * qty for name, qty in checkout_list.items())
        total = float(total)
        sales_tax = total * 0.10
        discount = 5 / 100 * total
        net_total = (total + sales_tax)
        if net_total > 5000:
            net_total -= discount
        print(f"Subtotal: ${total}")
        print("Sales tax: 10%")
        print(f'Discount amount: ${discount}')
        print(f'Sales tax amount: ${sales_tax}')
        print(f"Net total due: ${net_total}")
        payment = float(input("Please enter payment amount here: $"))
        payment = float(payment)

#Receipt Generation
        if payment >= net_total:
            change = (payment - net_total)
            print(" ")
            print(" ")
            print("~~~~~~~~~~~~~~~~~~~~~RECEIPT~~~~~~~~~~~~~~~~~~~~~")
            print("              Best Buy Retail Store")
            print("Items purchased:")
            show_cart()
            print(f"Subtotal: ${total}")
            print("Sales tax: 10%")
            print(f"Discount amount: ${discount}")
            print(f"Sales tax amount: ${sales_tax}")
            print(f"Net total due: ${net_total}")
            print(f"Amount paid: ${payment}")
            print(f"Your change is: ${change}")
            print(" ")
            print("Thank you for shopping with us.")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            print(" ")

#After checkout the program will clear the customer's cart and start over or terminate depending on user input
            new_customer= input("Press 'Y' if you would like to serve a new customer").strip().lower()
            if new_customer == 'y':
                checkout_list.clear()
                return
            else:
                import time
                print("Exiting.")
                time.sleep(1)
                print("Exiting..")
                time.sleep(1)
                print("Exiting...")
                checkout_list.clear()
                import sys
                sys.exit()


        else:
            print("insufficient amount entered.")
            return
    else:
        print("Checkout cancelled.")

#Welcome message
print("     Welcome to Best Buy Retail Store")
print("Please select an option from the menu below")

#Main menu options
def menu():
    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~MENU~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1. Show store items")
        print("2. Add item")
        print("3. Remove item")
        print("4. Show cart")
        print("5. Checkout")
        print("6. Exit")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        menu_option = input("Please select an option: ")
        if menu_option == '1':
            show_store()
        elif menu_option == '2':
            add_to_checkout()
        elif menu_option == '3':
            remove_from_checkout()
        elif menu_option == '4':
            show_cart()
        elif menu_option == '5':
            checkout()
        elif menu_option == '6':
            print("Thank you for shopping with us.")
            break
        else:
            print("Invalid option.")

#Program starts here with menu being displayed
menu()

