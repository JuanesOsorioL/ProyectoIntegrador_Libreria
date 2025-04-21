class UsuarioDTO:
    
    def __init__(self, id=None, nombre="", email="", telefono="", direccion="", fechaRegistro=None, rolId=None):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.fechaRegistro = fechaRegistro
        self.rolId = rolId

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

    def __str__(self):
        return (
            f"Usuario(id={self.id}, Nombre='{self.nombre}', Email='{self.email}', "
            f"Telefono='{self.telefono}', Direccion='{self.direccion}', "
            f"Fecha de Registro={self.fechaRegistro}, Rol ID ={self.rolId})"
        )