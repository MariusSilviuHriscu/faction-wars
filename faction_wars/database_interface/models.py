from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String,ForeignKey, Enum , JSON

from faction_wars.races.race_enum import RaceEnum
from faction_wars.troops.unit_stance import UnitStanceEnum

Base = declarative_base()


    
class Account(Base):
    __tablename__ = 'accounts'

    id  : Mapped[int] = mapped_column(primary_key= True)
    name : Mapped[str] = mapped_column(String(20), unique= True)
    password_hash : Mapped[str]
    email : Mapped[str] = mapped_column(String(20))
    
    player : Mapped['Player'] = relationship('Player', back_populates='players' , uselist = False)

class Player(Base):
    __tablename__ = 'players'
    
    id : Mapped[int] = mapped_column(primary_key = True)
    
    race : Mapped[Enum[RaceEnum]]
    
    account_id : Mapped[int] = mapped_column(ForeignKey('accounts.id'))
    cities : Mapped[list['City']] = relationship('Account' , back_populates= 'accounts')

class City(Base):
    __tablename__ = 'cities'
    
    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(20),default='New City')
    
    player_id : Mapped[int] = mapped_column(ForeignKey('players.id') )
    
    player : Mapped['Player'] = relationship('Player', back_populates = 'players' ,uselist = False)
    
    owned_garrisons : Mapped[list['Garrison']] = relationship('Garrison' , back_populates= 'garrisons')
class Garrison(Base):
    __tablename__ = 'garrisons'
    
    id : Mapped[int] = mapped_column(primary_key= True)
    stance : Mapped[Enum[UnitStanceEnum]]
    troop_json : Mapped[JSON] = mapped_column(type_=JSON,nullable= False)
    owner_city_id : Mapped[int] = mapped_column(ForeignKey('cities.id'))
    owner_city : Mapped['City'] = relationship('City',back_populates= 'cities',uselist = False)
    
    map_location_x : Mapped[int]
    map_location_y : Mapped[int]
    