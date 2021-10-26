from enum import unique
from sqlalchemy import Column, Integer, String, DateTime
from app.db import db

class Paciente(db.Model):
    __tablename__ = "pacientes"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    fecha_nacimiento = Column(DateTime)
    email = Column(String(50), nullable=False)
    obra_social = Column(String(50))
    numero_afiliado = Column(Integer)
    


    def __init__(self, nombre, apellido, fecha_nacimiento, email, obra_social=None, numero_afiliado=None):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.email = email
        self.obra_social = obra_social
        self.numero_afiliado = numero_afiliado