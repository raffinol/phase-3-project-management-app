#!/usr/bin/env python3

from prettycli import red, green
from db.models import Project, Engineers
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

engine = create_engine("sqlite:///db/projects-data.db")
Session = sessionmaker(bind=engine)
session = Session()


class Cli:
    def __init__(self):
        self.clear_screen(50)
        print(green("Welcome to Project Tracker!\n"))
        self.main_menu()

    def main_menu(self):
        self.clear_screen(4)
        print(green("Main menu \n"))
        print("1. See list of projects")
        print("2. See list of engineers")
        print("3. Create a new project")
        print("4. Update a project")
        print("5. Delete a project")
        print("6. Add a new engineer")
        print("7. Exit")
        user_input = input("\nPlease make a selection (1-7): ")
        self.clear_screen(50)

        self.handle_user_input(user_input)

    def handle_user_input(self, input):
        is_number = input.isdigit()
        if is_number:
            selection = int(input)
            if 1 <= selection <= 7:
                self.handle_selection(selection)
            else:
                print(red("Incorrect selection. Try again."))
                self.main_menu()
        else:
            print(red("Incorrect selection. Try again."))
            self.main_menu()

    def handle_selection(self, selection):
        if selection == 1:
            self.projects_list()
        elif selection == 2:
            self.engineers_list()
        elif selection == 3:
            self.create_project()
        elif selection == 4:
            self.update_project()
        elif selection == 5:
            self.delete_project()
        elif selection == 6:
            self.add_engineer()
        else:
            self.exit()

    def projects_list(self):
        projects = []

        for project in session.query(Project):
            projects.append({"id": project.id, "title": project.title})
        df = pd.DataFrame(projects)
        print(green("list of projects: \n"))
        print(df.to_string(index=False))
        self.clear_screen(4)
        print("1. See project details")
        print("2. Go back to main menu")
        sel = input("\nPlease make a selection (1 or 2): ")
        is_number = sel.isdigit()
        if is_number:
            selection = int(sel)
            if selection == 1:
                self.project_details()
            elif selection == 2:
                self.main_menu()
            else:
                print("\n")
                print(red("Option not available. Back to main menu."))
                self.main_menu()
        else:
            print("\n")
            print(red("Option not available. Back to main menu."))
            self.main_menu()

    def project_details(self):
        self.clear_screen(4)
        selection = input("Enter project ID to see details: ")
        project = session.query(Project).filter(Project.id == selection).first()
        if project:
            self.clear_screen(4)
            print(green("Selected project detail:"))
            print(project)
            self.main_menu()
        else:
            print(red("There is no project with that ID, back to main menu"))

    def engineers_list(self):
        engineers = []

        for engineer in session.query(Engineers):
            engineers.append({"id": engineer.id, "name": engineer.name})
        df = pd.DataFrame(engineers)
        print(green("list of engineers: \n"))
        print(df.to_string(index=False))
        self.clear_screen(4)
        print("1. See engineer details")
        print("2. See engineer assigned projects")
        print("3. Go back to main menu")
        sel = input("\nPlease make a selection (1-3): ")
        is_number = sel.isdigit()
        if is_number:
            selection = int(sel)
            if selection == 1:
                self.engineer_details()
            elif selection == 2:
                self.assigned_projects()
            elif selection == 3:
                self.main_menu()
            else:
                print("\n")
                print(red("Option not available. Back to main menu"))
                self.main_menu()
        else:
            print("\n")
            print(red("Option not available. Back to main menu."))
            self.main_menu()

    def engineer_details(self):
        self.clear_screen(4)
        selection = input("Enter engineer ID to see details: ")
        self.clear_screen(4)
        engineer = session.query(Engineers).filter(Engineers.id == selection).first()
        if engineer:
            engineer_data = [
                {
                    "id": engineer.id,
                    "name": engineer.name,
                    "last_name": engineer.last_name,
                    "level": engineer.level,
                }
            ]
            df = pd.DataFrame(engineer_data)
            print(df.to_string(index=False))
            self.main_menu()
        else:
            print(red("There is no engineer with that ID, back to main menu. "))
            self.main_menu()

    def assigned_projects(self):
        self.clear_screen(4)
        selection = input("Enter Engineer ID to see projects assigned: ")
        self.clear_screen(4)
        engineer = session.query(Engineers).filter(Engineers.id == selection).first()
        if engineer:
            projects = (
                session.query(Project).filter(Project.engineer_id == engineer.id).all()
            )
            if projects:
                projects_data = [
                    {
                        "id": projects.id,
                        "title": projects.title,
                    }
                    for projects in projects
                ]
                df = pd.DataFrame(projects_data)
                print(green("Projects assigned to selected engineer: \n"))
                print(df.to_string(index=False))
                self.main_menu()
            else:
                print(
                    red(
                        "This engineer doesn't have projects assigned, back to main menu. "
                    )
                )
                self.main_menu()
        else:
            print(red("There is no engineer with that ID, back to main menu. "))
            self.main_menu()

    def create_project(self):
        title = input("Enter new project title: ")
        description = input("Enter new project description: ")
        start_date = input("Enter new project start date: ")
        due_date = input("Enter new project due date: ")
        urgency = input("Enter new project urgency (low, medium or high): ")
        engineer_id = input("Enter engineer ID to be assigned: ")
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
        self.clear_screen(4)
        print(green("Project added"))
        self.main_menu()

    def update_project(self):
        selection = input("\nEnter project ID to update: ")
        project = session.query(Project).filter(Project.id == selection).first()
        if project:
            title = input("Enter new project title: ")
            description = input("Enter new project description: ")
            start_date = input("Enter new project start date: ")
            due_date = input("Enter new project due date: ")
            urgency = input("Enter new project urgency (low, medium or high): ")
            engineer_id = input("Enter new assigned engineer ID: ")
            project.title = title
            project.description = description
            project.start_date = start_date
            project.due_date = due_date
            project.urgency = urgency
            project.engineer_id = engineer_id
            session.add(project)
            session.commit()
            self.clear_screen(2)
            print(green("Project updated"))
            self.main_menu()
        else:
            print(red("Project doesn't exist\n"))
            self.main_menu()

    def delete_project(self):
        selection = input("\nEnter project ID to delete: ")
        project = session.query(Project).filter(Project.id == selection).first()
        if project:
            confirm = input(
                red(
                    f"\nAre you sure you want to delete project with ID {selection}? Y/N: "
                )
            )
            if confirm == "Y" or confirm == "y":
                session.query(Project).filter(Project.id == selection).delete()
                session.commit()
                self.clear_screen(4)
                print(green("Project deleted"))
                self.main_menu()
            elif confirm == "N" or confirm == "n":
                print("\nBack to main menu.")
                self.main_menu()
            else:
                print(red("\nOption not available. Back to main menu."))
                self.main_menu()
        else:
            print("\n")
            print(red("\nOption not available. Back to main menu."))
            self.main_menu()

    def add_engineer(self):
        name = input("Enter new engineer name: ")
        last_name = input("Enter new engineer last name: ")
        level = input("Enter new engineer level (junior, mid or senior): ")
        engineer = Engineers(
            name=name,
            last_name=last_name,
            level=level,
        )
        session.add(engineer)
        session.commit()
        self.clear_screen(4)
        print(green("Engineer added"))
        self.main_menu()

    def exit(self):
        print(green("goodbye!"))
        self.clear_screen(2)

    def clear_screen(self, lines):
        print("\n" * lines)


if __name__ == "__main__":
    Cli()
