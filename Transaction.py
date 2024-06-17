from sqlalchemy import Transaction
from database import Session, User


def add_transaction(user_id, amount, category, description):
    new_transaction = Transaction(user_id=user_id, amount=amount, category=category, description=description)
    Session.add(new_transaction)
    Session.commit()

# Example transaction
if User:
    add_transaction(User.user_id, 50.0, 'Groceries', 'Bought groceries at supermarket')
