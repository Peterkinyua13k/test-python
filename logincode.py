# Improved User Information System

def get_valid_age():
    while True:
        age = input("Enter your age: ")
        if age.isdigit():
            return age
        else:
            print("Age must be a number. Try again.")

def get_valid_email():
    while True:
        email = input("Enter your email: ")
        if "@" in email and "." in email:
            return email
        else:
            print("Invalid email format. Try again.")

print("=== User Registration System ===")

name = input("Enter your name: ")
age = get_valid_age()
country = input("Enter your country: ")
email = get_valid_email()
occupation = input("Enter your occupation: ")

print("\n--- User Details ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Country: {country}")
print(f"Email: {email}")
print(f"Occupation: {occupation}")

# Save data to file
with open("users.txt", "a") as file:
    file.write(f"{name}, {age}, {country}, {email}, {occupation}\n")

print("\n User data saved successfully!")
