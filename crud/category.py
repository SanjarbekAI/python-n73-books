from core.db_settings import execute_query


def add_category():
    title = input("Enter category title: ")
    # check if title exists or not
    query = "INSERT INTO category (title) VALUES (%s)"
    params = (title,)
    if execute_query(query=query, params=params):
        print("Category is added")
    else:
        print("Something getting wrong, try again!")


def delete_category():
    pass


def show_all_categories():
    pass
