import math

def display_trigonometric_table():
  # Define a list of common angles in degrees
  angles_in_degrees = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360]
  
  # Print the table header
  print(f"{'Angle':<8}{'Sin':<10}{'Cos':<10}{'Tan':<10}")
  print("-" * 38)
  
  # Iterate through the angles to calculate and print values
  for angle in angles_in_degrees:
    # Convert degrees to radians for math functions
    angle_rad = math.radians(angle)
    
    # Calculate sine and cosine
    sin_val = math.sin(angle_rad)
    cos_val = math.cos(angle_rad)
    
    # Handle the special case for tan(90) and tan(270)
    if angle % 180 == 90:
        tan_val = "Undefined"
    else:
        tan_val = f"{math.tan(angle_rad):.4f}"
        
    print(f"{angle:<8}{sin_val:<10.4f}{cos_val:<10.4f}{tan_val:<10}")

# Run the function to display the table
display_trigonometric_table()