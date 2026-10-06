# Online Shopping Cart - Final Project (Portfolio Project)
# Michael Freemon, CSU Global
# ItemToPurchase and ShoppingCart classes with a menu-driven program.
# The menu checks every entry so bad input asks again instead of crashing.


class ItemToPurchase:
    """One item in the shopping cart."""

    def __init__(self, item_name="none", item_price=0.0, item_quantity=0,
                 item_description="none"):
        """Set up the item. The defaults match the assignment."""
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        """Print the item's quantity, price, and line total."""
        # Example: Nike Romaleos 2 @ $189.00 = $378.00
        item_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ "
              f"${self.item_price:.2f} = ${item_cost:.2f}")

    def print_item_description(self):
        """Print the item's name and description."""
        # Example: Nike Romaleos: Volt color, Weightlifting shoes
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    """Holds the customer's info and a list of ItemToPurchase objects."""

    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        """Set up the cart with the default name, date, and an empty list."""
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        """Add an ItemToPurchase object to the cart."""
        self.cart_items.append(item)

    def remove_item(self, item_name):
        """Remove the item with this name, or say it was not found."""
        # Look for the item by name and remove the first match
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, new_item):
        """Update a matching item in the cart, or say it was not found."""
        # Only change the values that are not still set to the defaults
        for item in self.cart_items:
            if item.item_name == new_item.item_name:
                if new_item.item_description != "none":
                    item.item_description = new_item.item_description
                if new_item.item_price != 0:
                    item.item_price = new_item.item_price
                if new_item.item_quantity != 0:
                    item.item_quantity = new_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items(self):
        """Return the total quantity of all items in the cart."""
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        """Return the total cost of everything in the cart."""
        total_cost = 0.0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def print_total(self):
        """Print every item's cost and the cart total."""
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items()}")
        print()
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
        print()
        print(f"Total: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        """Print the description of every item in the cart."""
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()
        print("Item Descriptions")
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        for item in self.cart_items:
            item.print_item_description()


def get_text(prompt):
    """Ask for text until the user types something that is not blank."""
    text = input(prompt).strip()
    while text == "":
        print("This cannot be blank. Please try again.")
        text = input(prompt).strip()
    return text


def get_price(prompt):
    """Ask for a price until the user enters a number that is 0 or more."""
    while True:
        entry = input(prompt).strip()
        try:
            price = float(entry)
        except ValueError:
            print("Price must be a number, like 3.50. Please try again.")
            continue
        if price < 0:
            print("Price cannot be negative. Please try again.")
        else:
            return price


def get_quantity(prompt):
    """Ask for a quantity until the user enters a whole number of 1 or more."""
    while True:
        entry = input(prompt).strip()
        try:
            quantity = int(entry)
        except ValueError:
            print("Quantity must be a whole number, like 2. Please try again.")
            continue
        if quantity < 1:
            print("Quantity must be at least 1. Please try again.")
        else:
            return quantity


def print_menu(cart):
    """Show the menu and run the chosen option until the user quits."""
    menu = ("\nMENU\n"
            "a - Add item to cart\n"
            "r - Remove item from cart\n"
            "c - Change item quantity\n"
            "i - Output items' descriptions\n"
            "o - Output shopping cart\n"
            "q - Quit\n")
    valid_options = ["a", "r", "c", "i", "o", "q"]
    choice = ""

    # Keep showing the menu until the user quits
    while choice != "q":
        print(menu)
        choice = input("Choose an option: ").strip().lower()

        # Invalid choice: tell the user and ask again
        while choice not in valid_options:
            print("Invalid option. Please enter a, r, c, i, o, or q.")
            choice = input("Choose an option: ").strip().lower()

        if choice == "a":
            print("\nADD ITEM TO CART")
            name = get_text("Enter the item name: ")
            description = get_text("Enter the item description: ")
            price = get_price("Enter the item price: ")
            quantity = get_quantity("Enter the item quantity: ")
            cart.add_item(ItemToPurchase(name, price, quantity, description))

        elif choice == "r":
            print("\nREMOVE ITEM FROM CART")
            name = get_text("Enter name of item to remove: ")
            cart.remove_item(name)

        elif choice == "c":
            print("\nCHANGE ITEM QUANTITY")
            name = get_text("Enter the item name: ")
            quantity = get_quantity("Enter the new quantity: ")
            # Only the name and quantity are set, so modify_item
            # leaves the price and description alone
            cart.modify_item(ItemToPurchase(name, item_quantity=quantity))

        elif choice == "i":
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif choice == "o":
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()

    print("\nThanks for shopping. Goodbye!")


def main():
    """Get the customer's name and date, then start the menu."""
    customer_name = get_text("Enter customer's name: ")
    current_date = get_text("Enter today's date: ")
    print()
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)


if __name__ == "__main__":
    main()
