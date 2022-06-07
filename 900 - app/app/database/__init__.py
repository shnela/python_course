from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import Config

metadata = MetaData()
engine = create_engine(Config.db_connection_string)
Base = declarative_base(bind=engine, metadata=metadata)
Session = sessionmaker(bind=engine)
