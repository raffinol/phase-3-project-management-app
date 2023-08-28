# Project management CLI App
This is a CLI App built with python and using SQLAlchemy to create and manage the database. The App allows to keep track of a list of projects and a list of engineers and the relation between the two lists. As well ass to execute CRUD operations on both lists to result on a fully functional project tracking App.

## Installation
- Fork and clone this repo.
- Navigate to the repo folder and install dependencies by running: 

    `pipenv install`
- Start up the virtual environment by running:

    `pipenv shell`

### Seed Database
Repo has predetermined data in the database but there is also the option to seed the db by running the seed.py file:

```
cd lib
cd db
python3 seed.py
```
### Run CLI
Make sure you are in the lib folder and run:

`./cli.py`

**Enjoy the app!**

## How it works 
### Usage
From the main menu you can select 9 options:

1. See list of projects: Shows the id and title of the list of projects currently in the database. 
With a sub-option to see more details on a specific of the projects.
2. See list of engineers: Shows the id and name of the list of engineers currently in the database.
With a sub-option to see more details on a specific engineer and another sub-option to see projects assigned to a specific engineer.
3. Create a new project: Creates a new project based on user input. 
4. Update a project: Updates a project based on user input.
5. Delete a project: Deletes a project based on user selection.
6. Add a new engineer: Adds a new engineer based on user input.
7. Update engineer information: Updates engineer information based on user input.
8. Delete engineer: Deletes an engineer based on user selection.
9. Exit: Exit the app. 
### Files overview
Description of important files:
- In the root folder you will find pipfile and Pipfile.lock files that manages the virtual environment and the dependencies needed to run the application. 
- In the lib/db folder you will find alembic.ini, a generic database configuration file.
- In the lib/db folder you will find models.py that keeps the classes with the format to create the database tables.
- In the lib/db folder you will find the migration folders that contains a versions folder with the different modifications to the database structure. 
- In the lib/db folder you will find seed.py file that lets you seed the database with generic information for testing purposes.
- In the lib folder you will find the cli.py file that contains the python code to run the application that takes care of calling the database. 




