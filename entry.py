if __name__ == "__main__":
    import app as app
    from app.database import create_tables, get_session
    from app.database.models import UserCreate

    create_tables()

    user = UserCreate(
        name="samuel",
        email="sam@me.com",
        profession="teacher",
        city="barcelona",
        vehicule=False,
        seniority="2022-07-07",
    ).dict()

    app.add_user_file(user)

    users = app.load_json_file()

    app.add_users_to_database(users, get_session())

    app.get_users_from_database(get_session())

    mail_content = {
        "message": "This message has been sent from Python",
        "receiver_email": "acpytest@gmail.com",
        "subject": "[Test] Universidad Europea",
    }

    app.send_report(mail_content)
