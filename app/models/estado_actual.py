from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String
from app.db import db
from app.models.empleado import Empleado

class EstadoActual(db.Model):
    __tablename__ = "estado_actual"
    id = Column(Integer, primary_key=True)
    estado_actual = Column(Integer) #id del nombre del estado
    ultimo_cambio = Column(Integer) #id de empleado que realizó el último cambio
    
    def __init__(self):
        self.nombre = "ESPERANDO PRESUPUESTO"




"""def cambio_de_estado(id_estado, id_empleado):
    estado = Estado.query.get(id_estado)
    empleado = Empleado.query.get(id_empleado)
    estado.estado_actual = estado.estado_actual().sig
    estado.ultimo_cambio = empleado 

"""