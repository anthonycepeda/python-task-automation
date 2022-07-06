# Task Automation with Python

This app contains examples on how to:

- read and write on files (csv, json and xls)
- basic operations with databases
- working with emails
- data visualization

## Quick start:

### Run Script Mode:

```bash
    $ python3 -m venv .venv # create virtual environment
    $ source .venv/bin/activate # for windows: source .venv\Scripts\activate
    $ pip install pipenv
    $ pipenv install
    $ pipenv run python entry.py # run app
```

### Run WebApp

```bash
    $ python -m streamlit run webapp.py

    You can now view your Streamlit app in your browser.

    Local URL: http://localhost:8501
    Network URL: http://192.168.1.100:8501
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
    │   │
    ├── .gitignore
    ├── .dot.env.example
    ├── Pipfile
    ├── requirements.txt
    ├── docs/users.csv, users.json, users.xlsx, user.db
    └── README.md
```

#### TODO: data visualization modules

Help:

- [Python Basics](https://realpython.com/tutorials/basics/)
- [Working with Virtual Environments](https://www.youtube.com/watch?v=N5vscPTWKOk) - video
- [Streamlit Webapp Documentation](https://docs.streamlit.io/)
