import os


class Config:
    db_connection_string = os.getenv('DB_CONNECTION_STRING')
