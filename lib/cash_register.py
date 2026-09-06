#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount=0):
        # Set the discount when creating the cash register
        self.discount = discount

        # Start the total at zero
        self.total = 0

        # Start with an empty list of items
        self.items = []

        # Start with an empty list of previous transactions
        self.previous_transactions = []

    @property
    def discount(self):
        # Return the current discount
        return self._discount

    @discount.setter
    def discount(self, value):
        # Make sure discount is an integer between 0 and 100
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        # Add the price of all quantities to the total
        self.total += price * quantity

        # Add the item to the list once for each quantity
        for _ in range(quantity):
            self.items.append(item)

        # Store the transaction details
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        # There is no discount when the discount is zero
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        # Calculate the discount amount
        discount_amount = self.total * (self.discount / 100)

        # Subtract the discount from the total
        self.total -= discount_amount

        # Print the new total
        print(f"After the discount, the total comes to ${self.total:g}.")

    def void_last_transaction(self):
        # Do nothing if there are no transactions
        if not self.previous_transactions:
            return

        # Remove the last transaction
        transaction = self.previous_transactions.pop()

        # Subtract its cost from the total
        self.total -= transaction["price"] * transaction["quantity"]

        # Remove the items from the items list
        for _ in range(transaction["quantity"]):
            self.items.pop()