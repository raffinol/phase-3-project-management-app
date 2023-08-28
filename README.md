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



