from .models import Book, Author
from ariadne import convert_kwargs_to_snake_case


# resolve books will no longer exist?
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


# This will now display the author as well
@convert_kwargs_to_snake_case
def resolve_book(obj, info, book_id):
    try:
        book = Book.query.get(book_id)
        # resolve_author(obj=obj, info=info, author_id=book.author_id)
        payload = {
            "success": True,
            "book": book.to_dict()
        }

    except AttributeError:  # book not found
        payload = {
            "success": False,
            "errors": [f"Book item matching id {book_id} not found"]
        }

    return payload


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
