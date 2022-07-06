# Task Automation with Python

This app contains examples on how to:

- read and write on files (csv, json and xls)
- basic operations with databases
- working with emails
- data visualization

## Quick start:

```bash
    $ python3 -m venv .venv # create virtual environment
    $ source .venv/bin/activate # for windows: source .venv\Scripts\activate
    $ pip install pipenv
    $ pipenv install
    $ pipenv run python entry.py # run app
```

## Project Tree:

```bash
.
└── Trasks Automation with Python/
    ├── app/
    │   ├── __init__.py
    │   ├── database/
    │   │      ├── __init__.py
    │   │      ├── crud.py
    │   │      ├── models.py
    │   ├── files/
    │   │      ├── __init__.py
    │   │      ├── reader.py
    │   │      ├── writer.py
    │   ├── utlis/
    │   │      ├── logger.py
    │   ├── requirements/
    │   │      ├── requirements.txt
    ├── .gitignore
    ├── .dot.env.example
    ├── user.db
    ├── docs/users.csv, users.json, users.xlsx
    └── README.md
```

#### TODO: data visualization modules
