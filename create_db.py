from database import Base, engine
from models import Client


def create_tables():
    Base.metadata.create_all(bind=engine)
    
    
create_tables()
