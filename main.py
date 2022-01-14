from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, ObjectType, QueryType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify

from api import app
from api.mutations import resolve_create_book, resolve_delete_book, \
    resolve_create_author, resolve_delete_author, resolve_author_last_name
from api.queries import author_with_id, resolve_books_for_author, resolve_authors, \
    resolve_books, resolve_book, resolve_author

# binds
query = QueryType()
author = ObjectType("Author")
book = ObjectType("Book")

query.set_field("author_with_id", author_with_id)
author.set_field("books", resolve_books_for_author)

query.set_field("authors", resolve_authors)
query.set_field("author", resolve_author)
query.set_field("books", resolve_books)
query.set_field("book", resolve_book)

mutation = ObjectType("Mutation")
mutation.set_field("createBook", resolve_create_book)
mutation.set_field("deleteBook", resolve_delete_book)
mutation.set_field("createAuthor", resolve_create_author)
mutation.set_field("deleteAuthor", resolve_delete_author)
mutation.set_field("changeAuthorLastName", resolve_author_last_name)

type_defs = load_schema_from_path("schema.graphql")

schema = make_executable_schema(type_defs, [author, book, query, mutation])


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

    status_code = 200 if success else 400
    return jsonify(result), status_code
