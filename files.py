name = input("Enter your name: ")
with open("name.txt", 'w') as file:
    file.write(name)

with open("name.txt", 'r') as file:
    name = file.read().strip()
    print(f"Hi {name}!")

with open("numbers.txt", 'r') as file:
    numbers = file.readlines()
    total = int(numbers[0]) + int(numbers[1])
    print(f"The sum of the first two numbers is: {total}")

with open("numbers.txt", 'r') as file:
    total = sum(int(line) for line in file)
    print(f"The total of all numbers is: {total}")
