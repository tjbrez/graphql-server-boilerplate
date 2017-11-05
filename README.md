GraphQL Server Boilerplate Project
================================

This boilerplate project allows quick setup of a GraphQL server. This is accomplished through a combination of Graphene + Flask + SQLAlchemy. Out of the box it is setup to use a SQLite or PostgreSQL database. Enjoy!

Getting started
---------------

1. Clone this repo to your new project directory
2. If using virtualenv, activate the virtual environment
3. Run `pip install -r requirements.txt`
4. Create a `.env` file and add a database URL
5. Build your data model in the **models.py** file (A sample User model exists to get you started) 
6. Build your graphene schema in the **schema.py** file (A sample User SQLAlchemyObjectType exists to get you started) 
7. Run `python runserver.py`
8. Finally... go to [http://127.0.0.1:5000/graphql](http://127.0.0.1:5000/graphql) to see it action!
