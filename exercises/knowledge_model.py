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
	hits=Column(Integer)
	#num_q=Column(Integer, default=0)

	def __repr__(self):
		return ("Name: {}\n"
				"Topic: {}\n"
				"Rating: {}\n"
				"Hits:	{}\n"
				"ID: {}").format(
					self.name,
					self.topic,
					self.rating,
					self.hits,
					self.id_number)
