from sqlalchemy import TIMESTAMP, VARCHAR, Column, Integer
from app.database import Base


class BaseModel(Base):
    
    __abstract__ = True
    
    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    
class Product(BaseModel):
    __tablename__ = 'products'
    
    title = Column(VARCHAR(255), nullable=True)
    image = Column(VARCHAR(255), nullable=True)