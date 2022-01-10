from api import app
from api import models
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from api.queries import resolve_books, resolve_book, resolve_authors, resolve_author
from api.mutations import resolve_create_book, resolve_delete_book, \
                            resolve_create_author, resolve_delete_author  # , resolve_update_due_date

query = ObjectType("Query")
query.set_field("books", resolve_books)
query.set_field("book", resolve_book)
query.set_field("authors", resolve_authors)
query.set_field("author", resolve_author)


mutation = ObjectType("Mutation")
mutation.set_field("createBook", resolve_create_book)
mutation.set_field("deleteBook", resolve_delete_book)
# mutation.set_field("updateDueDate", resolve_update_due_date)
mutation.set_field("createAuthor", resolve_create_author)
mutation.set_field("deleteAuthor", resolve_delete_author)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)


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
