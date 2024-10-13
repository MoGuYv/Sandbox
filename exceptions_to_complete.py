is_valid_input = False
while not is_valid_input:
    try:
        result = int(input("Enter an integer: "))
        is_valid_input = True
    except ValueError:
        print("Invalid input. Please enter an integer.")
print(f"You entered: {result}")
