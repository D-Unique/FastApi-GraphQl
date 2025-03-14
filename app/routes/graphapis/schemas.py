from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL
from ariadne.asgi.handlers import GraphQLTransportWSHandler, GraphQLHTTPHandler


query = QueryType()

type_defs = """
    type Query {
        hello: String!
    }
"""

@query.field("hello")
def resolve_hello(*_):
    return "Hello Day 3!"

schema = make_executable_schema(type_defs, query)


# Create GraphQL App instance
graphql_app = GraphQL(
    schema,
    debug=True,
    http_handler=GraphQLHTTPHandler(),
    execute_get_queries=True,
    websocket_handler=GraphQLTransportWSHandler(),
)




