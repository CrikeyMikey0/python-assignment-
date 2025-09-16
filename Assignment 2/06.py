# Hardcoded credentials for comparison
correct_username = "mca_student"
correct_password = "password123"

# Prompt the user for input
username = input("Enter username: ")
password = input("Enter password: ")

# Compare the entered credentials
if username == correct_username and password == correct_password:
  print("Login successful! Welcome.")
else:
  print("Login failed. Incorrect username or password.")