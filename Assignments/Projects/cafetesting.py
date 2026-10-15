cafe_name = "Python Café"
tax_rate = 0.08

menu = {
    "chai": 3.00,
    "latte": 4.99,
    "sel": 4.99,
    "pizza": 7.99,
    "Burger": 8.99,
    "tea": 3.99,
}

order = []


def greet(name):
    print(f"Welcome to {cafe_name}, {name}!")

def show_menu(menu):
    print("---- Menu ----")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")

