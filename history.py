from database import Session, Transaction, User


def get_transaction_history(user_id):
    transactions = Session.query(Transaction).filter_by(user_id=user_id).order_by(Transaction.date).all()
    return transactions

# Example transaction history
if User:
    transactions = get_transaction_history(User.user_id)
    for transaction in transactions:
        print(f'{transaction.date}: {transaction.category} - ${transaction.amount} ({transaction.description})')
