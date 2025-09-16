from datetime import date, datetime

def get_age(birth_date_str):
    # Get today's date
    today = date.today()
    
    # Convert the birth date string to a date object
    birth_date = datetime.strptime(birth_date_str, "%d-%m-%Y").date()
    
    # Calculate the full years
    years = today.year - birth_date.year
    
    # Adjust years if the birthday hasn't occurred yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        years -= 1
    
    # Calculate months and days
    months = today.month - birth_date.month
    days = today.day - birth_date.day
    
    # Adjust for negative months or days
    if days < 0:
        months -= 1
        last_month = today.replace(day=1) - date.resolution
        days += last_month.day
    
    if months < 0:
        months += 12
    
    print(f"Birth Date: {birth_date_str}")
    print(f"Current Date: {today}")
    print(f"\nYour age is: {years} years, {months} months, and {days} days.")

# Your age is calculated here
get_age("18-02-2005")