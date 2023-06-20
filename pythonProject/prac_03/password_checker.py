

"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 8
MAX_LENGTH = 20
REQUIRES_SPECIAL_CHAR = True

while True:
    password = input("Enter your password: ")

    if len(password) < MIN_LENGTH:
        print(f"Password should be at least {MIN_LENGTH} characters long.")
    elif len(password) > MAX_LENGTH:
        print(f"Password should be at most {MAX_LENGTH} characters long.")
    elif not any(char.isdigit() for char in password):
        print("Password should contain at least one digit.")
    elif not any(char.islower() for char in password):
        print("Password should contain at least one lowercase letter.")
    elif not any(char.isupper() for char in password):
        print("Password should contain at least one uppercase letter.")
    elif REQUIRES_SPECIAL_CHAR and not any(not char.isalnum() for char in password):
        print("Password should contain at least one special character.")
    else:
        print("Password is valid.")
        break
