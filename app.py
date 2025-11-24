print("Welcome to my Python program!")

# Asking a user how much he slept
hours = input("How many hours did you sleep today? ")

# Ensuring it's a number
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()

# Converting hours to minutes
minutes = hours * 60
print(f"You've slept {minutes} minutes today.")