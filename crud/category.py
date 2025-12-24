from core.db_settings import execute_query
from crud.user import get_active_user


def add_category():
    user = get_active_user()
    title = input("Enter category title: ")
    # check if title exists or not
    query = "INSERT INTO category (user_id, title) VALUES (%s, %s)"
    params = (user['id'], title,)
    if execute_query(query=query, params=params):
        print("Category is added")
    else:
        print("Something getting wrong, try again!")


def delete_category():
    category_id = input("Enter category id: ")
    query = "DELETE FROM category WHERE (%s)"
    params = (category_id,)


def show_all_categories():
    user = get_active_user()
    query = "SELECT * FROM category WHERE user_id=%s;"
    params = (user['id'],)
    categories = execute_query(query=query, params=params, fetch="all")
    if categories:
        counter = 1
        for cat in categories:
            print(f"{counter}) {cat['id']}\t{cat['title']}")
            counter += 1
        return True

    else:
        print("No category")
        return None


