# Online Shopping Cart

This is my final Portfolio Project for my Python class at CSU Global.

## What it does

The program is a simple shopping cart that runs in the terminal. It asks for your name and the date, then shows a menu:

- a - Add item to cart
- r - Remove item from cart
- c - Change item quantity
- i - Output items' descriptions
- o - Output shopping cart
- q - Quit

It uses two classes. ItemToPurchase holds one item (name, price, quantity, and description). ShoppingCart holds the customer name, the date, and the list of items. The menu keeps running until you type q.

If you type something wrong, like a letter that is not on the menu, a price that is not a number, or a negative quantity, the program tells you and asks again. It does not crash.

## How to run it

You need Python 3. Download online_shopping_cart_final.py, open a terminal in that folder, and run:

```
python online_shopping_cart_final.py
```

On Windows you can also use `py online_shopping_cart_final.py`.

## Author

Michael Freemon
