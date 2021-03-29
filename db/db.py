from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://cctkeice:1WkUZWZaYO10afVD9zncn2MQ5pqbQ4-E@hattie.db.elephantsql.com:5432/cctkeice')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()