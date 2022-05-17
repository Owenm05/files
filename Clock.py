from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%D")
print("Current Time =", current_time)
print("Current Date =", current_date)
