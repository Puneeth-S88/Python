import re

def check_password_strength(password):
    strength = 0
    remarks = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters long")

    # Lowercase
    if re.search("[a-z]", password):
        strength += 1
    else:
        remarks.append("Add lowercase letters")

    # Uppercase
    if re.search("[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add uppercase letters")

    # Digits
    if re.search("[0-9]", password):
        strength += 1
    else:
        remarks.append("Add numbers")

    # Special characters
    if re.search("[@#$%^&*()!]", password):
        strength += 1
    else:
        remarks.append("Add special characters")

    # Strength result
    if strength == 5:
        return "Strong Password ✅", remarks
    elif strength >= 3:
        return "Medium Password ⚠️", remarks
    else:
        return "Weak Password ❌", remarks


# Main program
password = input("Enter your password: ")

result, suggestions = check_password_strength(password)

print("\nResult:", result)

if suggestions:
    print("Suggestions:")
    for s in suggestions:
        print("-", s)