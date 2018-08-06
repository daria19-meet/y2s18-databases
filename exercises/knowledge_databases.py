from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

session.query(Knowledge).delete()

def add_article(name, topic, rating):
	adding=Knowledge(
		topic=topic,
		name=name,
		rating=rating)
	session.add(adding)
	session.commit()

add_article("Rainbow", "Weather", 8 )
add_article("Black holes", "Space", 10)
add_article("Chocolate", "Food", 6)

def query_all_articles():
	articles = session.query(Knowledge).all()
	return articles

#print(query_all_articles())

def query_article_by_topic(topic):
	chosen_topic = session.query(
       Knowledge).filter_by(
       topic=topic).all()
	return chosen_topic

#print(query_article_by_topic("Weather"))

def query_article_by_rating(threshhold):
	articles=session.query(Knowledge).filter(Knowledge.rating<threshhold).all()
	return articles

# print(query_article_by_rating(7))

def query_article_by_primary_key(searching):
	chosen=session.query(Knowledge).filter_by(id_number=searching)
	return chosen

print(query_article_by_primary_key(1))

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
