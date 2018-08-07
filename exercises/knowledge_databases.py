from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

session.query(Knowledge).delete()

def add_article(name, topic, rating,hits):
	adding=Knowledge(
		topic=topic,
		name=name,
		rating=rating,
		hits=hits)
	session.add(adding)
	session.commit()

add_article("Black holes", "Space", 10,5)
add_article("Chocolate", "Food", 6,2)
add_article("Rainbow", "Weather", 8, 7)

def query_all_articles():
	articles = session.query(Knowledge).all()
	return articles

print(query_all_articles())

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
	chosen=session.query(Knowledge).filter_by(id_number=searching).first()
	return chosen

#print(query_article_by_primary_key(1))

def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(topic=topic).delete()
	session.commit

#delete_article_by_topic("Weather")


def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()

#delete_all_articles()

def edit_article_rating(updated, name):
	article=session.query(Knowledge).filter_by(name=name).first()
	article.rating=(updated+article.rating)/2
	session.commit()

#edit_article_rating(8, "Black holes")	


def delete_by_rating(threshhold):
	articles=query_article_by_rating(threshhold)
	for checking in articles:
		session.query(Knowledge).filter_by(id_number=checking.id_number).delete()
	session.commit()

def top_five():
	all_articles=session.query(Knowledge).order_by(Knowledge.rating.desc()).all()
	return all_articles





print(top_five())
