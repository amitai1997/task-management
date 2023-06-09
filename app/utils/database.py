# import psycopg2
# from flask import current_app, g
# from app.app import app


# def get_db_connection():
#     with app.app_context():
#         if 'db' not in g:
#             g.db = psycopg2.connect(
#                 # host=app.app.config['DB_HOST'],
#                 # port=current_app.config['DB_PORT'],
#                 # user=current_app.config['DB_USER'],
#                 # password=current_app.config['DB_PASSWORD'],
#                 # database=current_app.config['DB_NAME']
#                 # TODO configure with config.py and .env file
#                 host='localhost',
#                 port='5432',
#                 user='postgres',
#                 password='example',
#                 database='billing_system'
#             )
#         return g.db


# def close_db_connection():
#     db = g.pop('db', None)
#     if db is not None:
#         db.close()
