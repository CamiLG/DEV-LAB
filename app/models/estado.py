from sqlalchemy.sql.sqltypes import String
from app.db import db
from sqlalchemy import Column, Integer
class Estado(db.Model):
    __tablename__ = "estados"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))

    def __init__(self, nombre):
        self.nombre = nombre