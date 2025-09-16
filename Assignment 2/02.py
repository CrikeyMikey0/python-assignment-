import time

def epoch():
    # Get total seconds since the epoch
    seconds = time.time()
    
    # Calculate hours and remaining minutes
    hours = int(seconds / 3600)
    minutes = int((seconds % 3600) / 60)
    
    print(f"Total seconds since epoch: {seconds}")
    print(f"Time since epoch: {hours} hours and {minutes} minutes")

# Run the function
epoch()