from core.db_settings import execute_query
from crud.category import show_all_categories


def add_book():
    if show_all_categories() is None:
        return None
    category_id = input("Enter category id: ")
    # check this id is existing or not

    name = input("Enter book name: ")
    author = input("Enter book author: ")
    note = input("Enter note: ")
    status = input("Enter book status(done,ongoing,new): ")
    query = "INSERT INTO books (category_id, name, author, note, status) VALUES (%s, %s, %s, %s, %s)"
    params = (category_id, name, author, note, status,)
    if execute_query(query=query, params=params):
        print("Books is added")
        return None
    else:
        print("Something getting wrong, please try again later")
        return True


def delete_book():
    pass


def search_book():
    """search with name, note, author"""
    pass


def show_all_books():
    pass
