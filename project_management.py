"""project_management.py - Menu-based project management program."""

from project import Project


def load_projects(filename):
    projects = []
    with open(filename, "r") as file:
        file.readline()  # skip header
        for line in file:
            parts = line.strip().split('\t')
            projects.append(Project(*parts))
    return projects


def save_projects(filename, projects):
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tPercent Complete\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate}\t{project.percent_complete}\n")


def display_projects(projects):
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]
    print("Incomplete projects:")
    for p in sorted(incomplete):
        print(f"  {p}")
    print("Completed projects:")
    for p in sorted(complete):
        print(f"  {p}")


def filter_projects_by_date(projects, date_str):
    filter_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered = [p for p in projects if p.start_date > filter_date]
    for p in sorted(filtered, key=lambda x: x.start_date):
        print(p)


def add_project():
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percent_complete = int(input("Percent complete: "))
    return Project(name, start_date, priority, cost_estimate, percent_complete)


def update_project(projects):
    for i, p in enumerate(projects):
        print(f"{i} {p}")
    index = int(input("Project choice: "))
    project = projects[index]
    print(project)
    new_pc = input("New Percentage: ")
    new_priority = input("New Priority: ")
    project.update(new_pc if new_pc else None,
                   new_priority if new_priority else None)


def main():
    import datetime
    FILENAME = "projects.txt"
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)

    menu = "\n- (L)oad  - (S)ave  - (D)isplay  - (F)ilter  - (A)dd  - (U)pdate  - (Q)uit"
    print(menu)
    while True:
        choice = input(">>> ").lower()
        if choice == "l":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date_str)
        elif choice == "a":
            new_project = add_project()
            projects.append(new_project)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            save = input(f"Would you like to save to {FILENAME}? ").lower()
            if save in ("yes", "y"):
                save_projects(FILENAME, projects)
            print("Goodbye!")
            break
        else:
            print("Invalid choice")
        print(menu)


if __name__ == "__main__":
    main()
