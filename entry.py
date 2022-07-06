if __name__ == "__main__":
    import app as app
    from app.database import create_database_tables, get_session
    from app.database.models import UserCreate

    # using UserCreate Model to create an user
    user = UserCreate(
        name="samuel",
        email="sam@me.com",
        profession="teacher",
        city="barcelona",
        vehicule=False,
        seniority="2022-07-07",
    ).dict()

    app.add_user_to_file(user, "users.xlsx")

    # load users
    users = app.load_file("users.json")
    create_database_tables()

    # adding users to database
    app.add_users_to_database(users, get_session())

    # getting users from database
    app.get_users_from_database(get_session())

    mail_content = {
        "message": "This message has been sent from Python",
        "receiver_email": "acpytest@gmail.com",
        "subject": "[Test] Universidad Europea",
    }

    # sending an email
    app.send_report(mail_content)
