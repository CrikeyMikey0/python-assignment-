import hashlib

def hash_password(password):
  # Hashes the password by converting it to bytes and applying SHA-256
  return hashlib.sha256(password.encode()).hexdigest()

# Define correct credentials
correct_username = "mca_student"
correct_password = "password123"

# Hash the correct password once at the start
correct_hashed_password = hash_password(correct_password)

# Get user input
username = input("Enter username: ")
password = input("Enter password: ")

# Hash the user's password for comparison
user_hashed_password = hash_password(password)

# Compare credentials
if username == correct_username and user_hashed_password == correct_hashed_password:
  print("Login successful! Welcome.")
else:
  print("Login failed. Incorrect username or password.")