import pickle

def save_projects_pickle(filename, projects):
    with open(filename, "wb") as file:
        pickle.dump(projects, file)


def load_projects_pickle(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)


def main():
    FILENAME = "projects.pkl"
    try:
        projects = load_projects_pickle(FILENAME)
        print("Loaded projects from pickle.")
    except FileNotFoundError:
        projects = []

    for project in projects:
        print(project)

    save_projects_pickle(FILENAME, projects)
    print("Saved projects to pickle.")


if __name__ == "__main__":
    main()
