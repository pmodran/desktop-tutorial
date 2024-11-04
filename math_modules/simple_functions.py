from datetime import datetime

def seconds_until(future_date _str):
    # Parse the future date string into a datetime object
    future_date = datetime.strptime(future_date_str, '%Y%m%d%H%M%S')
    
    # Get the current date and time
    current_date = datetime.now()
    
    # Calculate the difference in seconds
    delta = future_date - current_date
    return delta.total_seconds()

