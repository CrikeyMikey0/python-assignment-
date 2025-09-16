import random

def generate_random_numbers(count):
  """Generates a specified number of random integers."""
  
  print(f"Generating {count} random numbers:")
  for i in range(count):
      # Generate a random integer between 1 and 100 (inclusive)
      random_number = random.randint(1, 100)
      print(random_number)

# Call the function to generate 10 random numbers
generate_random_numbers(10)