from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.sql.expression import null
from app.db import db

class Empleado(db.Model):
    __tablename__ = "empleados"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    usuario = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    rol = Column(Enum("ADMINISTRADOR", "EMPLEADO"), nullable=False, default="ADMINISTRADOR")
    


    def __init__(self, nombre, apellido, usuario, email, password, rol):
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.email = email
        self.password = password
        self.rol = rol