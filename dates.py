from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta

now = datetime.now()

timestamp = now.timestamp()
print(f"The timestamp is: {timestamp}") # This is the number of seconds since the epoch (January 1, 1970)

year_2025 = datetime(2025, 1, 1) # Is necessary to specify the year, month, and day

def print_date(date):
    print(f"The date is: {date}")
    print(f"The year is: {date.year}")
    print(f"The month is: {date.month}")
    print(f"The day is: {date.day}")
    print(f"The hour is: {date.hour}")
    print(f"The minute is: {date.minute}")
    print(f"The second is: {date.second}")
    print(f"The weekday is: {date.weekday()}")  # Note: weekday() returns 0 for Monday and 6 for Sunday
    print(f"The timestamp now is: {date.timestamp()}")

# print_date(year_2025)

current_time = time() # Encapsulates the time without the date

current_time = time(12, 30, 45) # Specify hour, minute, second
print(f"The current time is: {current_time}")
print(f"The hour is: {current_time.hour}")
print(f"The minute is: {current_time.minute}")
print(f"The second is: {current_time.second}")

current_date = now.date()  # Get the current date from the datetime object

current_date = date(year_2025.year, year_2025.month + 1, year_2025.day)  # Create a date object from the datetime object

# current_time.hour = 15  # This will raise an error because time objects are immutable

print(f"The current date is: {current_date}")

start_timedelta = timedelta(200, 100, 100, weeks=2)  # Create a timedelta object with 200 days, 100 seconds, 100 microseconds, and 2 weeks
end_timedelta = timedelta(300, 100, 100, weeks=8)  # Create another timedelta object

print(end_timedelta - start_timedelta)  # Subtract the two timedelta objects
print(start_timedelta + end_timedelta)  # Add the two timedelta objects
print(start_timedelta * 2)  # Multiply the timedelta by 2
print(start_timedelta / 2)  # Divide the timedelta by 2