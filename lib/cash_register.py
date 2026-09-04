#!/usr/bin/env python3

class CashRegister:

    # Create a new cash register
    # Discount is optional and defaults to 0
    def __init__(self, discount=0):
        self.discount = discount

        # Keep track of the current total price
        self.total = 0

        # Store the names of items added to the register
        self.items = []

        # Store details about each transaction
        self.previous_transactions = []

    # Getter for the discount
    # Allows us to access the discount using cash_register.discount
    @property
    def discount(self):
        return self._discount

    # Setter for the discount
    # Checks that the discount is an integer between 0 and 100
    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            # Print an error if the discount is not valid
            print("Not valid discount")

    # Add an item to the cash register
    def add_item(self, item, price, quantity=1):

        # Add the price of the items to the total
        self.total += price * quantity

        # Add the item to the items list once for each quantity
        for _ in range(quantity):
            self.items.append(item)

        # Save the transaction details
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    # Apply the discount to the current total
    def apply_discount(self):

        # Check if there are any transactions
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        # Calculate how much money should be discounted
        discount_amount = self.total * (self.discount / 100)

        # Subtract the discount from the total
        self.total -= discount_amount

        # Display the new total after applying the discount
        print(f"After the discount, the total comes to ${self.total:g}.")

    # Remove the most recent transaction
    def void_last_transaction(self):

        # Do nothing if there are no previous transactions
        if not self.previous_transactions:
            return

        # Remove and store the last transaction
        transaction = self.previous_transactions.pop()

        # Subtract the removed transaction's cost from the total
        self.total -= transaction["price"] * transaction["quantity"]

        # Remove the item from the items list for each quantity
        for _ in range(transaction["quantity"]):
            self.items.pop()
