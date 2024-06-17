import hashlib

from database import Session, User

def register_user(username, email, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    new_user = User(username=username, email=email, password=hashed_password)
    Session.add(new_user)
    Session.commit()

def login_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user = Session.query(User).filter_by(username=username, password=hashed_password).first()
    return user

# Example registration
register_user('john_doe', 'john@example.com', 'password123')

# Example login
user = login_user('john_doe', 'password123')
if user:
    print(f'Logged in as {user.username}')
else:
    print('Invalid credentials')
