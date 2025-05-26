from Dtos.RolDTO import RolDTO
class UsuarioDTO:
    
    def __init__(self, id=None, nombre=None, email=None, telefono=None, direccion=None, fechaRegistro=None, rolId=None, rolDTO: RolDTO = None):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.fechaRegistro = fechaRegistro
        self.rolId = rolId
        self.rolDTO = rolDTO

    def Get_Id(self):
        return self.id

    def Get_Nombre(self):
        return self.nombre

    def Get_Email(self):
        return self.email

    def Get_Telefono(self):
        return self.telefono

    def Get_Direccion(self):
        return self.direccion

    def Get_FechaRegistro(self):
        return self.fechaRegistro

    def Get_RolId(self):
        return self.rolId

    def Set_Id(self, value):
        self.id = value

    def Set_Nombre(self, value):
        self.nombre = value

    def Set_Email(self, value):
        self.email = value

    def Set_Telefono(self, value):
        self.telefono = value

    def Set_Direccion(self, value):
        self.direccion = value

    def Set_FechaRegistro(self, value):
        self.fechaRegistro = value

    def Set_RolId(self, value):
        self.rolId = value

    def Get_RolDTO(self) -> RolDTO:
        return self.rolDTO

    def Set_RolDTO(self, value: RolDTO) -> None:
        self.rolDTO = value

    def to_dict_simple(self):
        return {
            "id":             self.Get_Id(),
            "nombre":         self.Get_Nombre(),
            "email":          self.Get_Email(),
            "telefono":       self.Get_Telefono(),
            "direccion":      self.Get_Direccion(),
            "fechaRegistro":  self.Get_FechaRegistro(),
            "rolId":          self.Get_RolId()
        }

    def to_dict(self):
        return {
            "id":             self.Get_Id(),
            "nombre":         self.Get_Nombre(),
            "email":          self.Get_Email(),
            "telefono":       self.Get_Telefono(),
            "direccion":      self.Get_Direccion(),
            "fechaRegistro":  self.Get_FechaRegistro(),
            "rolId":          self.Get_RolId(),
            "RolDTO": self.Get_RolDTO().to_dict()
        }