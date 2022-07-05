if __name__ == "__main__":
    import app as app
    from app.database import create_tables, get_session

    create_tables()
    app.write_a_file()
    users = app.load_a_file()
    app.add_users_to_database(users, get_session())
    app.get_users_from_database(get_session())
    mail_content = {
        "message": "This message has been sent from Python",
        "receiver_email": "acpytest@gmail.com",
        "subject": "[Test] Universidad Europea",
    }
    app.send_report(mail_content)
