from datetime import datetime

def calculate_date_difference(start_date_str, end_date_str):
    # Define the date format
    date_format = "%Y-%m-%d"
    
    # Convert date strings to datetime objects
    start_date = datetime.strptime(start_date_str, date_format)
    end_date = datetime.strptime(end_date_str, date_format)
    
    # Calculate the difference
    difference = end_date - start_date
    
    # Print the results
    print(f"Start Date: {start_date_str}")
    print(f"End Date: {end_date_str}")
    print(f"\nTime Difference:")
    print(f"Total Days: {difference.days}")
    print(f"Total Seconds: {difference.total_seconds()}")

# Example Usage
calculate_date_difference("2023-01-01", "2024-03-15")