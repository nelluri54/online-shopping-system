class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

class ShoppingCart:
    def __init__(self):
        self.items = {}  

    def add_item(self, product, quantity):
        if product.product_id in self.items:
            self.items[product.product_id] += quantity
        else:
            self.items[product.product_id] = quantity

    def remove_item(self, product, quantity):
        if product.product_id in self.items:
            self.items[product.product_id] -= quantity
            if self.items[product.product_id] <= 0:
                del self.items[product.product_id]

    def calculate_total(self):
        total = 0
        for product_id, quantity in self.items.items():
            product = get_product_by_id(product_id) 
            total += product.price * quantity
        return total

class User:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.shopping_cart = ShoppingCart()
        self.order_history = []

    def add_to_cart(self, product, quantity):
        self.shopping_cart.add_item(product, quantity)

    def remove_from_cart(self, product, quantity):
        self.shopping_cart.remove_item(product, quantity)

    def checkout(self):
        total = self.shopping_cart.calculate_total()
        order = {"cart": self.shopping_cart.items.copy(), "total": total}
        self.order_history.append(order)
        self.shopping_cart.items.clear()

def get_product_by_id(product_id):
    products = [
        Product(1, "Laptop", 1000, 10),
        Product(2, "Phone", 500, 20),
        # Add more products as needed
    ]
    
    for product in products:
        if product.product_id == product_id:
            return product
    return None

def login(username, password):
    # Implement a simple authentication mechanism
    sample_users = {"user1": "password1", "user2": "password2"}
    if username in sample_users and sample_users[username] == password:
        return True
    else:
        return False

# Example usage:
# Assuming you have some products and a user
product1 = Product(1, "Laptop", 1000, 10)
product2 = Product(2, "Phone", 500, 20)

username = input("Enter username: ")
password = input("Enter password: ")

if login(username, password):
    user = User(1, username, password)

    # User adds products to the cart
    user.add_to_cart(product1, 2)
    user.add_to_cart(product2, 3)

    # User removes a product from the cart
    user.remove_from_cart(product1, 1)

    # User checks out
    user.checkout()

    # Accessing order history
    print("Order History:")
    for order in user.order_history:
        print(order)
else:
    print("Please check your username and password.")
