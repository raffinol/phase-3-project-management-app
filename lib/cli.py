from prettycli import red, green
from db.models import Project
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///db/projects-data.db")
Session = sessionmaker(bind=engine)
session = Session()


def main_menu():
    print("Welcome to Project Tracker!\n")
    print("1. See list of projects")
    print("2. Exit")
    user_input = input("Please make a selection (1-3)\n")

    handle_user_input(user_input)


def handle_user_input(input):
    is_number = input.isdigit()
    if is_number:
        selection = int(input)
        if 1 <= selection <= 2:
            handle_selection(selection)
    else:
        print(red("Incorrect selection\n"))
        main_menu()


def handle_selection(selection):
    if selection == 1:
        projects_list()
    else:
        exit()


def projects_list():
    projects = []

    for project in session.query(Project):
        projects.append({"id": project.id, "title": project.title})
    print(projects)


def exit():
    print(green("good bye!"))


main_menu()
