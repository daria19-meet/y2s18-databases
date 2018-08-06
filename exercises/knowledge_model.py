from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__="Knowledge"
	id_number=Column(Integer,primary_key=True)
	topic=Column(String)
	name=Column(String)
	rating=Column(Integer)

	def __repr__(self):
		if self.rating<=7:
			return("Unfortunately, this article does not have a better rating. Maybe, this is an article that should bereplaced soon")
		else:
			return(print("If you want to learn about", self.topic, ", we recommend you read the Wikipedia page", self.name,". We gave it a", self.rating, "out of 10!"))