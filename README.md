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
    │   ├── main.py
    │   ├── database/
    │   │      ├── __init__.py
    │   │      ├── crud.py
    │   │      ├── models.py
    │   ├── files/
    │   │      ├── docs/users.csv, users.json, users.xls
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
    └── README.md
```

#### TODO: data visualization modules
