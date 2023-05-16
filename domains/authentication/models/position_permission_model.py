from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class PositionPermissionModel(Base):
    __tablename__ = 'position_permission'

    position_permission_id = Column(String(45), primary_key=True)
    position_id = Column(String(45), ForeignKey('PositionModel.position_id'))
    permission_id = Column(String(45), ForeignKey('PermissionModel.permission_id'))
