from sqlalchemy.sql.sqltypes import String
from app.db import db
from sqlalchemy import Column, Integer

class Factura(db.Model):
    __tablename__ = "facturas"
    id = Column(Integer, primary_key=True)
    id_estudio = Column(Integer)
    archivo = Column(String(50)) #Buscar como indicar que es un pdf (Binario o algo así)
    id_obra_social = Column(Integer) #id de la obra social

    def __init__(self, id_estudio, archivo, id_obra_social=None):
        self.id_estudio = id_estudio
        self.archivo = archivo
        self. id_obra_social = id_obra_social