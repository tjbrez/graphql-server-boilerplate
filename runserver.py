#!/usr/bin/env python
import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask
from database import db_session
from flask_graphql import GraphQLView
from schema import schema

load_dotenv(find_dotenv(), verbose=True)
app = Flask(__name__)
app.config['DEBUG'] = os.environ.get('DEBUG', True)
app.config['DATABASE_URL'] = os.environ.get(
    'DATABASE_URL',
    'sqlite:///database.sqlite3'
)
app.add_url_rule(
    '/graphql', view_func=GraphQLView.as_view(
        'graphql', schema=schema, graphiql=True
    )
)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run()
