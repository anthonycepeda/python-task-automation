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
    $ pip install -r requirements/requirements.txt # install packages
    $ python entry.py # run app
```

## Project Tree:

```bash
.
└── Trasks Automation with Python/
    ├── app/
    │   ├── main.py
    │   ├── database/
    │   │      ├── __init__.py
    │   │      ├── user.db
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
    └── README.md
```

#### TODO: emails and data visualization modules
