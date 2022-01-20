from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, ObjectType, QueryType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify

from api import app

from api.queries import  \
    resolve_book, \
    resolve_books, \
    resolve_author, \
    resolve_authors, \
    resolve_publisher, \
    resolve_publishers

# binds
query = QueryType()

# book = ObjectType("Book")
# author = ObjectType("Author")
# publisher = ObjectType("Publisher")

query.set_field("book", resolve_book)
query.set_field("books", resolve_books)
query.set_field("author", resolve_author)
query.set_field("authors", resolve_authors)
query.set_field("publisher", resolve_publisher)
query.set_field("publishers", resolve_publishers)


# author.set_field("books", resolve_books_for_author)
# author.set_field("books", resolve_books_for_author_id)

# query.set_field("resolve_books_for_publisher", resolve_books_for_publisher)
# book.set_field("books", resolve_books_for_publisher)

# publisher.set_field("authors", resolve_authors_for_publisher)


type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(type_defs, query)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    print("\nIn main graphql_server: ")
    print("Success is: ", success)
    print("result is: ", result)
    print("\n\n")

    # status_code = 200 if success else 400
    return jsonify(result), 200
