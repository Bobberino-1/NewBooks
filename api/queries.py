from .models import Book, Author, Publisher
from ariadne import convert_kwargs_to_snake_case
from api import db

# resolvers
@convert_kwargs_to_snake_case
def resolve_book(obj, info, book_id):
    print("in queries - resolve_book - book_id is: ", book_id)
    book = Book.query.get(book_id)
    return book


@convert_kwargs_to_snake_case
def resolve_books(obj, info):
    print("in queries - resolve_books")
    books = [book.to_dict() for book in Book.query.all()]
    return books


@convert_kwargs_to_snake_case
def resolve_author(obj, info, author_id):
    print("in queries - resolve_author - author_id is: ", author_id)
    author = Author.query.get(author_id)
    return author


@convert_kwargs_to_snake_case
def resolve_authors(obj, info):
    print("in queries - resolve_authors")
    authors = [author.to_dict() for author in Author.query.all()]
    return authors


@convert_kwargs_to_snake_case
def resolve_publisher(_, info, publisher_id):
    print("In queries - resolve_publisher - publisher_id is: ", publisher_id)
    publisher = Publisher.query.get(publisher_id)
    return publisher

@convert_kwargs_to_snake_case
def resolve_publishers(obj, info):
    print("in queries - resolve_publishers")
    publishers = [publisher.to_dict() for publisher in Publisher.query.all()]
    return publishers


