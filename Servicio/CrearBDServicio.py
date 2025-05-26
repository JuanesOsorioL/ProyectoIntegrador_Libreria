from Repositorios.CrearBDRepositorio import CrearBDRepositorio
from Dtos.Generico.Respuesta import Respuesta
from Servicio.RolServicio import RolServicio
from Dtos.RolDTO import RolDTO

class CrearBDServicio:

    def __init__(self):
        self.repo = CrearBDRepositorio()

    def creartablasprocedimientos(self) -> Respuesta:
        # 1. DROP
        ok, msg = self.repo.drop_tables()
        if not ok:
            return Respuesta("Error Sistema", msg, [])

        # 2. CREATE TABLES
        ok, msg = self.repo.create_tables()
        if not ok:
            return Respuesta("Error Sistema", msg, [])

        # 3. CREATE PROCS
        ok, msg = self.repo.create_procedures()
        if not ok:
            return Respuesta("Error Sistema", msg, [])

        # 4. INSERTAR ROLES INICIALES
        for nombre in ("Administrador", "Empleado", "cliente"):
            rolDTO = RolDTO(None, nombre)
            resp = RolServicio.insertarRol(rolDTO)
            if not (isinstance(resp, Respuesta) and resp.get_estado() == "Operación Exitosa"):
                return Respuesta(
                    "Error Sistema",
                    f"Error al insertar rol '{nombre}': {resp.get_msj()}",
                    []
                )

        return Respuesta(
            "Operación Exitosa",
            "Tablas, procedimientos y roles iniciales creados correctamente.",
            [])