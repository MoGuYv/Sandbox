"""Project management program for CP1404 Practical 07.

Estimate time: 2.5 hours
Actual time:   (fill this in after finishing)
"""

from datetime import datetime
from project import Project

DEFAULT_FILENAME = "projects.txt"
DATE_FORMAT = "%d/%m/%Y"


def main():
    """Run the project management menu-driven program."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    menu = (
        "- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit"
    )

    print(menu)
    choice = input(">>> ").strip().lower()
    while choice != "q":
        if choice == "l":
            filename = input("Filename to load from: ").strip()
            if filename:
                try:
                    projects = load_projects(filename)
                    print(f"Loaded {len(projects)} projects from {filename}")
                except FileNotFoundError:
                    print("File not found.")
        elif choice == "s":
            filename = input("Filename to save to: ").strip()
            if filename:
                save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        else:
            print("Invalid choice")

        print(menu)
        choice = input(">>> ").strip().lower()

    # On quit, optionally save to default file
    answer = input(f"Would you like to save to {DEFAULT_FILENAME}? ").strip().lower()
    if answer.startswith("y"):
        save_projects(DEFAULT_FILENAME, projects)
    else:
        print("no, I think not.")
    print("Thank you for using custom-built project management software.")
    print("Ready for Kivy?")


def load_projects(filename):
    """Load projects from a tab-separated file into a list of Project objects."""
    projects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            line = line.strip()
            if not line:
                continue
            # Expected format:
            # Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage
            name, date_string, priority_text, cost_text, completion_text = line.split("\t")
            start_date = datetime.strptime(date_string, DATE_FORMAT).date()
            priority = int(priority_text)
            cost_estimate = float(cost_text)
            completion = int(completion_text)
            project = Project(name, start_date, priority, cost_estimate, completion)
            projects.append(project)
    return projects


def save_projects(filename, projects):
    """Save projects to a tab-separated file with a header line."""
    with open(filename, "w", encoding="utf-8") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            date_string = project.start_date.strftime(DATE_FORMAT)
            print(
                f"{project.name}\t{date_string}\t{project.priority}\t"
                f"{project.cost_estimate}\t{project.completion}",
                file=out_file,
            )
    print(f"Projects saved to {filename}")


def display_projects(projects):
    """Display incomplete and completed projects, sorted by priority."""
    incomplete_projects = [project for project in projects if not project.is_complete()]
    complete_projects = [project for project in projects if project.is_complete()]

    incomplete_projects.sort()
    complete_projects.sort()

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in complete_projects:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Ask for a date and show projects that start after that date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ").strip()
    try:
        filter_date = datetime.strptime(date_string, DATE_FORMAT).date()
    except ValueError:
        print("Invalid date format.")
        return

    filtered_projects = [project for project in projects if project.start_date >= filter_date]
    filtered_projects.sort(key=lambda p: p.start_date)

    for project in filtered_projects:
        print(project)


def add_new_project(projects):
    """Prompt the user for project details and add a new Project."""
    print("Let's add a new project")
    name = input("Name: ").strip()
    if not name:
        print("Name cannot be blank.")
        return

    date_string = input("Start date (dd/mm/yyyy): ").strip()
    try:
        start_date = datetime.strptime(date_string, DATE_FORMAT).date()
    except ValueError:
        print("Invalid date format; project not added.")
        return

    try:
        priority = int(input("Priority: "))
        cost_estimate = float(input("Cost estimate: $"))
        completion = int(input("Percent complete: "))
    except ValueError:
        print("Invalid number; project not added.")
        return

    project = Project(name, start_date, priority, cost_estimate, completion)
    projects.append(project)


def update_project(projects):
    """Allow user to choose a project and update its completion and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
    except (ValueError, IndexError):
        print("Invalid project choice.")
        return

    print(project)
    new_completion_text = input("New Percentage: ").strip()
    if new_completion_text:
        try:
            project.completion = int(new_completion_text)
        except ValueError:
            print("Invalid completion percentage; left unchanged.")

    new_priority_text = input("New Priority: ").strip()
    if new_priority_text:
        try:
            project.priority = int(new_priority_text)
        except ValueError:
            print("Invalid priority; left unchanged.")


if __name__ == "__main__":
    main()
