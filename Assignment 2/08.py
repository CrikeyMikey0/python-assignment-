import hashlib

def hash_password(password):
  """Hashes a password using SHA-256 for secure storage."""
  # Hashes the password by converting it to bytes and applying the SHA-256 algorithm
  hashed_password = hashlib.sha256(password.encode()).hexdigest()
  return hashed_password

# Define a username and password to authenticate against
correct_username = "mca_student"
correct_password = "password123"

# Hash the correct password once at the start of the program
correct_hashed_password = hash_password(correct_password)

# Get username and password input from the user
username = input("Enter username: ")
password = input("Enter password: ")

# Hash the password provided by the user
user_hashed_password = hash_password(password)

# Compare the entered username and the hashed passwords
if username == correct_username and user_hashed_password == correct_hashed_password:
  print("Login successful! Welcome.")
else:
  print("Login failed. Incorrect username or password.")