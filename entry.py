if __name__ == "__main__":
    import app as app
    from app.database import create_tables

    create_tables()
    # app.write_a_file()
    users = app.load_a_file()
    app.add_users_to_database(users)
    app.get_users_from_database()
