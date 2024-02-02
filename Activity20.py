# Case 1:


def addProducts(cart, storec):
    print('Select Product which product you want to add')

    for key, value in storec.items():
        print(f"Product: {key}, Price: {value}")

    flag = 'y'

    while flag.lower() == 'y':
        name = input("Enter name of the Product: ")
        if name in storec:
            cart[name] = float(storec[name][1:])  
            flag = input("Want to add more items (Y/N): ")
        else:
            print("Invalid product name. Please select a valid product.")

def displayCart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("\nYour Shopping Cart:")
        for key, value in cart.items():
            print(f"Product: {key}, Price: ${value:.2f}")
        print()

def removeCart(cart):
    if not cart:
        print("Your cart is already empty.")
        return

    pname = input('Enter product name to remove: ')
    if pname in cart:
        del cart[pname]
        print(f"{pname} has been removed from your cart.\n")
    else:
        print(f"{pname} not found in your cart.\n")

def totalCart(cart):
    total = sum(cart.values())
    print(f"Total Price of the cart is ${total:.2f}\n")

def checkoutCart(cart):
    if not cart:
        print("Your cart is empty. Nothing to checkout.")
        return

    print('\nThe summary of your purchase is:')
    displayCart(cart)
    totalCart(cart)
    print('Cart summary:')
    displayCart(cart)
    cart.clear()
    print("Your cart has been cleared.\n")

def exitCart():
    print('Exiting the shopping cart.\n')

def main():
    cart = {}
    storec = {
        'acer': '$300',
        'hp': '$500',
        'apple': '$1000',
        'Lenovo': '$400',
        'Dell': '$550'
    }

    print("Welcome to the Online shopping cart!\n")

    while True:
        print("Select operations:")
        print("1. Add Products")
        print("2. Display Cart")
        print("3. Remove Product from Cart")
        print("4. Calculate Total Price")
        print("5. Checkout")
        print("6. Exit System")

        choice = input("Enter Option: ")

        if choice == '1':
            addProducts(cart, storec)
        elif choice == '2':
            displayCart(cart)
        elif choice == '3':
            removeCart(cart)
        elif choice == '4':
            totalCart(cart)
        elif choice == '5':
            checkoutCart(cart)
        elif choice == '6':
            exitCart()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.\n")

if __name__ == "__main__":
    main()
