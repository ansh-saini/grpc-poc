from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import scoped_session, sessionmaker, Session

connection_string = 'postgresql://postgres:postgres@localhost:5432/local_db'
engine = create_engine(connection_string)


Base = automap_base()
Base.prepare(engine, reflect=True)

# Move to models.py
Users = Base.classes.users_users


session = Session(engine)
