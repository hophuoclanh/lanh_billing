from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class UserPositionModel(Base):
    __tablename__ = 'user_position'

    user_position_id = Column(String(45), primary_key=True)
    user_id = Column(String(45), ForeignKey('user.user_id'))
    position_id = Column(String(45), ForeignKey('position.position_id'))

