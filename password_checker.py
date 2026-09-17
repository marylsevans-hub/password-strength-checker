# Password Strength Checker
# Created as a beginner Python cybersecurity project.
# This program evaluates a password using five security requirements:
# length, uppercase letters, lowercase letters, numbers, and special characters.
# It provides a strength score and recommendations for improvement.

import getpass
print("Password Strength Checker")

password = getpass.getpass("Enter a password to check: ")

print("Your password contains", len(password), "characters.")

if len(password) >= 12:
    print("✓ Good length: Your password has at least 12 characters.")
else:
    print("✗ Too short: Your password should have at least 12 characters.")


if any(char.isupper() for char in password):
    print("✓ Uppercase letter found.")
else:
    print("✗ Add at least one uppercase letter.")
if any(char.islower() for char in password):
    print("✓ Lowercase letter found.")
else:
    print("✗ Add at least one lowercase letter.")

if any(char.isdigit() for char in password):
    print("✓ Number found.")
else:
    print("✗ Add at least one number.")
special_characters = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"

if any(char in special_characters for char in password):
    print("✓ Special character found.")
else:
    print("✗ Add at least one special character.")
score = 0

if len(password) >= 12:
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(char.islower() for char in password):
    score += 1

if any(char.isdigit() for char in password):
    score += 1

if any(char in special_characters for char in password):
    score += 1

print("\nPassword Strength Score:", score, "/ 5")

if score <= 2:
    print("Overall Strength: Weak")
elif score <= 4:
    print("Overall Strength: Moderate")
else:
    print("Overall Strength: Strong")
print("\nRecommendation:")

if score == 5:
    print("Your password meets all recommended requirements.")
elif score >= 3:
    print("Your password is fairly strong, but review the missing requirements above.")
else:
    print("Your password needs improvement. Review the missing requirements above before using it.")