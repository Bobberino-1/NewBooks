from ariadne import convert_kwargs_to_snake_case

from api import db
from api.models import Book, Author


@convert_kwargs_to_snake_case
def resolve_create_book(obj, info, name, author_id):
    try:
        book = Book(
            name=name,
            author_id=author_id
        )
        db.session.add(book)
        db.session.commit()
        payload = {
            "success": True,
            "book": book.to_dict()
        }
    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"There is an error in the input data"]
        }

    return payload


@convert_kwargs_to_snake_case
def resolve_delete_book(obj, info, book_id):
    try:
        book = Book.query.get(book_id)
        db.session.delete(book)
        db.session.commit()
        payload = {"success": True}

    except Exception as error:
        payload = {
            "success": False,
            "errors": [f"Todo matching id {book_id} not found. {error}"]
        }

    return payload


@convert_kwargs_to_snake_case
def resolve_create_author(obj, info, first_name, last_name):
    try:
        author = Author(
            first_name=first_name,
            last_name=last_name
        )
        db.session.add(author)
        db.session.commit()
        payload = {
            "success": True,
            "author": author.to_dict()
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [f"There is an error in the input data. {error}"]
        }

    return payload


@convert_kwargs_to_snake_case
def resolve_delete_author(obj, info, author_id):
    try:
        author = Author.query.get(author_id)
        db.session.delete(author)
        db.session.commit()
        payload = {"success": True}

    except Exception as error:
        payload = {
            "success": False,
            "errors": [f"Todo matching id {author_id} not found. {error}"]
        }

    return payload


'''
@convert_kwargs_to_snake_case
def resolve_update_due_date(obj, info, todo_id, new_date):
    try:
        todo = Todo.query.get(todo_id)
        if todo:
            todo.due_date = datetime.strptime(new_date, '%d-%m-%Y').date()
        db.session.add(todo)
        db.session.commit()
        payload = {
            "success": True,
            "todo": todo.to_dict()
        }

    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": ["Incorrect date format provided. Date should be in "
                       "the format dd-mm-yyyy"]
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": [f"Todo matching id {todo_id} not found"]
        }
    return payload
'''
