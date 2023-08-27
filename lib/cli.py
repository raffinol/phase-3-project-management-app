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
        self.main_menu()

    def main_menu(self):
        print("\nWelcome to Project Tracker!\n")
        print("1. See list of projects")
        print("2. See list of engineers")
        print("3. create a new project")
        print("4. Update a project")
        print("5. Delete a project")
        print("6. Exit")
        user_input = input("Please make a selection (1-6): ")

        self.handle_user_input(user_input)

    def handle_user_input(self, input):
        is_number = input.isdigit()
        if is_number:
            selection = int(input)
            if 1 <= selection <= 6:
                self.handle_selection(selection)
            else:
                print(red("Incorrect selection\n"))
                self.main_menu()
        else:
            print(red("Incorrect selection\n"))
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
        else:
            self.exit()

    def projects_list(self):
        projects = []

        for project in session.query(Project):
            projects.append({"id": project.id, "title": project.title})
            df = pd.DataFrame(projects)
        print(df.to_string(index=False))
        print("\n1. See project details")
        print("2. Go back to main menu")
        sel = input("Please make a selection (1 or 2): ")
        is_number = sel.isdigit()
        if is_number:
            selection = int(sel)
        if selection == 1:
            self.project_details()
        elif selection == 2:
            self.main_menu()
        else:
            print(red("Option not available. Back to main menu"))
            self.main_menu()

    def project_details(self):
        selection = input("Enter project ID to see details: ")
        project = session.query(Project).filter(Project.id == selection).first()
        print(project)
        self.main_menu()

    def engineers_list(self):
        engineers = []

        for engineer in session.query(Engineers):
            engineers.append({"id": engineer.id, "name": engineer.name})
            df = pd.DataFrame(engineers)
        print(df.to_string(index=False))
        print("\n1. See Engineer details")
        print("2. See engineer assigned projects")
        print("3. Go back to main menu")
        sel = input("Please make a selection (1-3): ")
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
            print(red("Option not available. Back to main menu"))
        self.main_menu()

    def engineer_details(self):
        selection = input("Enter Engineer ID to see details: ")
        engineer = session.query(Engineers).filter(Engineers.id == selection).first()
        print(engineer)
        self.main_menu()

    def assigned_projects(self):
        selection = input("Enter Engineer ID to see details: ")
        engineer = session.query(Engineers).filter(Engineers.id == selection).first()
        if engineer:
            projects = (
                session.query(Project).filter(Project.engineer_id == engineer.id).all()
            )
            projects_data = [
                {
                    "id": projects.id,
                    "title": projects.title,
                }
                for projects in projects
            ]
            df = pd.DataFrame(projects_data)
            print(df.to_string(index=False))

    def create_project(self):
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
        self.main_menu()

    def update_project(self):
        selection = input("Enter project ID to update: ")
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
        else:
            print(red("Project doesn't exist\n"))
            self.main_menu()

    def delete_project(self):
        selection = input("Enter project ID to delete: ")
        confirm = input(
            red(f"Are you sure you want to delete project with ID {selection}? Y/N: ")
        )
        if confirm == "Y" or confirm == "y":
            session.query(Project).filter(Project.id == selection).delete()
            session.commit()
            self.main_menu()
        elif confirm == "N" or confirm == "n":
            self.delete_project()
        else:
            print(red("wrong selection, back to main menu"))
            self.main_menu()

    def exit(self):
        print(green("goodbye!"))


if __name__ == "__main__":
    Cli()
