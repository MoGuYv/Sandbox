

from guitar import Guitar


def load_guitars(filename):
    guitars = []
    with open(filename, "r") as file:
        for line in file:
            name, year, cost = line.strip().split(",")
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def save_guitars(filename, guitars):
    with open(filename, "w") as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def display_guitars(guitars):
    print("These are the guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")


def add_guitars():
    guitars = []
    print("Enter your guitars (hit Enter to finish):")
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
    return guitars


def main():
    filename = "guitars.csv"
    guitars = load_guitars(filename)
    display_guitars(guitars)

    new_guitars = add_guitars()
    guitars.extend(new_guitars)
    guitars.sort()

    print("\nGuitars after adding and sorting:")
    display_guitars(guitars)

    save_guitars(filename, guitars)


if __name__ == "__main__":
    main()
