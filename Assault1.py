import csv
import random

FILENAME = 'places.csv'
UNVISITED = 'n'
VISITED = 'v'

def load_places():
    """Load places from CSV file."""
    places = []
    with open(FILENAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            row[2] = int(row[2])  # Convert priority to int
            places.append(row)
    return places

def save_places(places):
    """Save places to CSV file."""
    with open(FILENAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(places)

def display_places(places):
    """Display formatted list of places, sorted by visited status and priority."""
    places.sort(key=lambda x: (x[3] == VISITED, -x[2]))  # Sort by visited and priority
    unvisited_count = 0
    for i, place in enumerate(places, 1):
        visited_marker = '*' if place[3] == UNVISITED else ' '
        print(f"{i}. {place[0]:<20} in {place[1]:<15} Priority: {place[2]} {visited_marker}")
        if place[3] == UNVISITED:
            unvisited_count += 1
    print(f"\n{unvisited_count} places left to visit")

def recommend_place(places):
    """Recommend a random place to visit."""
    unvisited_places = [place for place in places if place[3] == UNVISITED]
    if unvisited_places:
        recommended = random.choice(unvisited_places)
        print(f"How about you visit {recommended[0]} in {recommended[1]} (Priority: {recommended[2]})?")
    else:
        print("No places left to visit!")

def add_place(places):
    """Add a new place to the list."""
    name = input("Name: ")
    country = input("Country: ")
    priority = get_positive_integer("Priority: ")
    places.append([name, country, priority, UNVISITED])
    print(f"{name} in {country} (Priority: {priority}) added to the list")

def mark_visited(places):
    """Mark a place as visited."""
    unvisited_places = [place for place in places if place[3] == UNVISITED]
    if not unvisited_places:
        print("No unvisited places")
        return

    display_places(places)
    place_num = get_positive_integer("Enter the number of a place to mark as visited: ")
    if 1 <= place_num <= len(places) and places[place_num-1][3] == UNVISITED:
        places[place_num-1][3] = VISITED
        print(f"{places[place_num-1][0]} marked as visited")
    else:
        print("Invalid choice")

def get_positive_integer(prompt):
    """Get a positive integer from the user with error checking."""
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
            else:
                print("Number must be > 0")
        except ValueError:
            print("Invalid input; enter a valid number")

def main():
    """Main program function."""
    print("Travel Tracker 1.0 - by [Your Name]")
    places = load_places()
    while True:
        print("\nMenu:")
        print("L - List places")
        print("R - Recommend a place")
        print("A - Add new place")
        print("M - Mark a place as visited")
        print("Q - Quit")
        choice = input(">>> ").upper()
        if choice == 'L':
            display_places(places)
        elif choice == 'R':
            recommend_place(places)
        elif choice == 'A':
            add_place(places)
        elif choice == 'M':
            mark_visited(places)
        elif choice == 'Q':
            save_places(places)
            print(f"{len(places)} places saved to {FILENAME}")
            break
        else:
            print("Invalid menu choice")

if __name__ == '__main__':
    main()
