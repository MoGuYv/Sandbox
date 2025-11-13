"""More Guitars - load from CSV, allow user to add, then save back."""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read guitars from a file, display them, allow user to add more, then save."""
    guitars = load_guitars(FILENAME)

    print("These are my guitars:")
    display_guitars(guitars)

    print("\nAdd new guitars (blank name to quit):")
    guitars = add_new_guitars(guitars)

    print("\nSorted guitars (oldest to newest):")
    guitars.sort()  # uses Guitar.__lt__
    display_guitars(guitars)

    save_guitars(FILENAME, guitars)


def load_guitars(filename):
    """Load guitars from CSV file into a list of Guitar objects."""
    guitars = []
    with open(filename, "r", encoding="utf-8") as in_file:
        for line in in_file:
            line = line.strip()
            if not line:
                continue
            name, year_text, cost_text = line.split(",")
            guitar = Guitar(name, int(year_text), float(cost_text))
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    """Display guitars in a numbered list."""
    for i, guitar in enumerate(guitars, start=1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar}{vintage_string}")


def add_new_guitars(guitars):
    """Prompt user to add new guitars and append them to the list."""
    while True:
        name = input("Name: ").strip()
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
    return guitars


def save_guitars(filename, guitars):
    """Save the list of guitars back to CSV file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
    print(f"\n{len(guitars)} guitars saved to {filename}")


if __name__ == "__main__":
    main()
