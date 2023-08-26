from prettycli import red, green
from db.models import Project, Engineers
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

engine = create_engine("sqlite:///db/projects-data.db")
Session = sessionmaker(bind=engine)
session = Session()


def main_menu():
    print("Welcome to Project Tracker!\n")
    print("1. See list of projects")
    print("2. See list of engineers")
    print("3. create a new project")
    print("4. Update a project")
    print("5. Delete a project")
    print("6. Exit")
    user_input = input("Please make a selection (1-6): ")

    handle_user_input(user_input)


def handle_user_input(input):
    is_number = input.isdigit()
    if is_number:
        selection = int(input)
        if 1 <= selection <= 6:
            handle_selection(selection)
        else:
            print(red("Incorrect selection\n"))
            main_menu()
    else:
        print(red("Incorrect selection\n"))
        main_menu()


def handle_selection(selection):
    if selection == 1:
        projects_list()
    elif selection == 2:
        engineers_list()
    elif selection == 3:
        create_project()
    elif selection == 4:
        update_project()
    elif selection == 5:
        delete_project()
    else:
        exit()


def projects_list():
    projects = []

    for project in session.query(Project):
        projects.append({"id": project.id, "title": project.title})
        df = pd.DataFrame(projects)
    print(df.to_string(index=False))
    print("\n")
    main_menu()


def engineers_list():
    engineers = []

    for engineer in session.query(Engineers):
        engineers.append({"id": engineer.id, "name": engineer.name})
        df = pd.DataFrame(engineers)
    print(df.to_string(index=False))
    print("\n")
    main_menu()


def create_project():
    title = input("Enter project title: ")
    description = input("Enter project description: ")
    start_date = input("Enter project start date: ")
    due_date = input("Enter project due date: ")
    urgency = input("Enter project urgency (low, medium or high): ")
    engineer_id = input("Enter the assigned engineer ID: ")
    project = Project(
        title=title,
        description=description,
        start_date=start_date,
        due_date=due_date,
        urgency=urgency,
        engineer_id=engineer_id,
    )
    session.add(project)
    session.commit()
    print(green("Project added"))
    main_menu()


def update_project():
    selection = input("Enter project ID to update: ")
    title = input("Enter new project title: ")
    description = input("Enter new project description: ")
    start_date = input("Enter new project start date: ")
    due_date = input("Enter new project due date: ")
    urgency = input("Enter new project urgency (low, medium or high): ")
    engineer_id = input("Enter new assigned engineer ID: ")
    for project in session.query(Project):
        if project.id == int(selection):
            project.title = title
            project.description = description
            project.start_date = start_date
            project.due_date = due_date
            project.urgency = urgency
            project.engineer_id = engineer_id
            session.add(project)
            session.commit()
        else:
            print(red("Project doesn't exist\n"))
            main_menu()


def delete_project():
    selection = input("Enter project ID to delete: ")
    confirm = input(
        red(f"Are you sure you want to delete project with ID {selection}? Y/N: ")
    )
    if confirm == "Y" or confirm == "y":
        session.query(Project).filter(Project.id == selection).delete()
        session.commit()
    elif confirm == "N" or confirm == "n":
        delete_project()
    else:
        print(red("wrong selection, back to main menu"))
        main_menu()


def exit():
    print(green("goodbye!"))


main_menu()
