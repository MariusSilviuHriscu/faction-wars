from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import String,ForeignKey, create_engine

engine = create_engine("sqlite:///mydatabase.db", echo=True)


Base = declarative_base()


class Email(Base):
    
    __tablename__ = 'emails'
    id : Mapped[int] = mapped_column(primary_key=True)
    email_string : Mapped[str] = mapped_column(String(20))
    user_id : Mapped[int] = mapped_column(ForeignKey('users.id'))
    user : Mapped['User'] = relationship('User',back_populates='email',uselist= False )

class User(Base):
    
    __tablename__ = 'users'
    
    id : Mapped[int] = mapped_column(primary_key= True)
    name : Mapped[str]
    
    email: Mapped[list['Email']] = relationship('Email', back_populates='user')


def make_classes():
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        
        
        email1 = Email(email_string = 'lala',
                       )
        
        email2 = Email(email_string = 'dudu',
                       )
        
        user1 = User(name = 'iona',
                     email = [email1,email2]
                     )
        
        session.add(user1)
        
        session.commit()


        
def main():
    make_classes()

main()