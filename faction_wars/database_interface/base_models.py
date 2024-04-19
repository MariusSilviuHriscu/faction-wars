from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship



Base = declarative_base()



class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password_hash = Column(String)
    player_id = Column(Integer, ForeignKey('players.id'))

    player = relationship("Player", back_populates="account")

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    cities = relationship("City", backref="player", cascade="all, delete-orphan")

    account = relationship("Account", uselist=False, back_populates="player")


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String, default='new town')
    x_coord = Column(Float)
    y_coord = Column(Float)
    point_value = Column(Integer)
    owner = Column(String)
    inner_city_id = Column(Integer, ForeignKey('inner_cities.id'))

    player_id = Column(Integer, ForeignKey('players.id'))
    player = relationship("Player", back_populates="cities")

class InnerCity(Base):
    __tablename__ = 'inner_cities'

    id = Column(Integer, primary_key=True)
    # Add other fields as needed
    city_id = Column(Integer, ForeignKey('cities.id'))