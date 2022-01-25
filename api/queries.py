from .models import Book, Author
from ariadne import convert_kwargs_to_snake_case
from api import db


# resolvers
def author_with_id(_, info, author_id):
    author = Author.query.get(author_id)
    return author


# Remember that if a resolver returns a value that is of another
# type defined in the schema, we need to implement a resolver
# for that field as well.
def resolve_books_for_author(author, info):
    books = db.session.query(Book.id, Book.name).join(Author, Book.author_id == Author.id). \
        filter(Book.author_id == author.id).all()
    return books


@convert_kwargs_to_snake_case
def resolve_authors(obj, info):
    try:
        authors = [author.to_dict() for author in Author.query.all()]
        payload = {
            "success": True,
            "authors": authors
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def resolve_books(obj, info):
    try:
        books = [book.to_dict() for book in Book.query.all()]
        payload = {
            "success": True,
            "books": books
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def resolve_book(obj, info, book_id):
    try:
        book = Book.query.get(book_id)
        payload = {
            "success": True,
            "book": book,
        }
    except Exception as error:  # book not found
        payload = {
            "success": False,
            "errors": [f"{error}"]
            # "errors": [f"Book item matching id {book_id} not found"]
        }

    return payload


@convert_kwargs_to_snake_case
def resolve_author(obj, info, author_id):
    try:
        author = Author.query.get(author_id)
        payload = {
            "success": True,
            "author": author.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": [f"Author item matching id {author_id} not found"]
        }
    return payload
