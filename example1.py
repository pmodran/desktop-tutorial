from datetime import datetime, timedelta

def count_working_days(start_date, end_date):
    current_date = start_date
    working_days = 0

    while current_date <= end_date:
        if current_date.weekday() < 5:  # Monday to Friday are considered working days
            working_days += 1
        current_date += timedelta(days=1)

    return working_days

# Example usage
start_date_str = input("Enter the start date (YYYY-MM-DD): ")
end_date_str = input("Enter the end date (YYYY-MM-DD): ")

start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

working_days = count_working_days(start_date, end_date)
print(f"There are {working_days} working days between {start_date_str} and {end_date_str}.")