print("Welcome to my Python program!")
hours = input("How many hours did you sleep today? ")
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()

minutes = hours * 60
print(f"You've slept {minutes} minutes today.")