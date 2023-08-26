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
    print("3. Exit")
    user_input = input("Please make a selection (1-3)\n")

    handle_user_input(user_input)


def handle_user_input(input):
    is_number = input.isdigit()
    if is_number:
        selection = int(input)
        if 1 <= selection <= 3:
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


def exit():
    print(green("goodbye!"))


main_menu()
