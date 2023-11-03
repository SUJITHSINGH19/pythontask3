import re

def password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = bool(re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\]', password))

    if length > 8 and has_upper and has_lower and has_digit and has_special:
        return "Strong"
    elif length > 6 and has_upper and has_lower and (has_digit or has_special):
        return "Medium"
    else:
        return "Weak"

# Get user input for the password
password = input("Enter your password: ")

# Determine the strength and provide a visual indicator
strength = password_strength(password)
if strength == "Strong":
    print("Password is strong 🔒")
elif strength == "Medium":
    print("Password is medium 🔐")
else:
    print("Password is weak 🔓")
