from sqlalchemy.sql.sqltypes import String
from app.db import db
from sqlalchemy import Column, Integer

class Muestra(db.Model):
    __tablename__ = "muestras"
    id = Column(Integer, primary_key=True)
    numero_lote = Column(Integer)
    id_estudio = Column(Integer)

    def __init__(self, numero_lote, id_estudio):
        self.numero_lote = numero_lote
        self.id_estudio = id_estudio