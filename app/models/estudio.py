from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import DateTime
from app.db import db

class Estudio(db.Model):
    __tablename__ = "estudios"
    id = Column(Integer, primary_key=True)
    id_paciente = Column(Integer)
    id_medico_derivante = Column(String(50), nullable=False)
    tipo_estudio = Column(Enum("EXOMA-GENOMA", "MITOCONDRIAL-COMPLETO", "CARRIER DE ENFERMEDADES MONOGENICAS RECESIVAS", "CARRIOTIPO-ARRAY-CGH"), nullable=False, default="EXOMA-GENOMA")
    fecha_alta = Column(DateTime)
    id_estado_actual = Column(Integer) #Id del estado actual del estudio
    diagnostico_presuntivo = Column(String(200))
    id_muestra = Column(Integer) #Id de la muestra

    def __init__(self, id_paciente, id_medico_derivante, tipo_estudio, fecha_alta, id_estado_actual, diagnostico_presuntivo, id_muestra):
        self.id_paciente = id_paciente
        self.id_medico_derivante = id_medico_derivante
        self.tipo_estudio = tipo_estudio
        self.fecha_alta = fecha_alta
        self.id_estado_actual = id_estado_actual
        self.diagnostico_presuntivo = diagnostico_presuntivo
        self.id_muestra = id_muestra