#!/usr/bin/env python3
class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.transactions = []

    def add_item(self, title, price, quantity=1):
        # Add item to the total based on quantity
        self.total += price * quantity
        # Add items to the items list based on quantity
        self.items.extend([title] * quantity)
        # Store the last transaction for voiding
        self.transactions.append(price * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.transactions:
            # Subtract the last transaction from the total
            last_transaction = self.transactions.pop()
            self.total -= last_transaction
        if self.total < 0:
            self.total = 0  # Ensure the total can't go negative
