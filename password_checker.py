MIN_LENGTH = 5
MAX_LENGTH = 15
REQUIRES_SPECIAL_CHAR = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def is_valid_password(password):
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_special = any(char in SPECIAL_CHARACTERS for char in password)

    if REQUIRES_SPECIAL_CHAR:
        return has_digit and has_upper and has_lower and has_special
    else:
        return has_digit and has_upper and has_lower


password = input("Enter your password: ")
while not is_valid_password(password):
    print("Invalid password. Please try again.")
    password = input("> ")

print(f"Your password '{password}' is valid.")
