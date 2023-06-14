from .models import User
from . import db

# Create a new User instance
user = User(username='john_doe', email='john@example.com', password='password123')

# Add the user to the session
db.session.add(user)

try:
    # Commit the changes
    db.session.commit()
    print("User created successfully!")
except:
    # Rollback the changes if an exception occurs
    db.session.rollback()
    print("Failed to create user. Rolling back changes.")
