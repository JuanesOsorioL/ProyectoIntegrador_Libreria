from Servicio.CrearBDServicio import CrearBDServicio
from Dtos.Generico.Respuesta import Respuesta

crearBDServicio=CrearBDServicio();

class CrearBDControlador:

    def creartablasprocedimientos() -> Respuesta:
        return crearBDServicio.creartablasprocedimientos()