from datetime import date

class Usuario:
    def __init__(self, id_rol=None, codigo_usuario=None, nombre=None, apellido=None, email=None,
                 telefono=None, direccion=None, fecha_registro=None, fecha_expiracion=None, activo=True, id=None):
        self._id = id
        self._id_rol = id_rol
        self._codigo_usuario = codigo_usuario
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono
        self._direccion = direccion
        self._fecha_registro = fecha_registro or date.today()
        self._fecha_expiracion = fecha_expiracion
        self._activo = activo

    # Getters y Setters usando property
    @property
    def id(self):
        return self._id

    @property
    def id_rol(self):
        return self._id_rol

    @id_rol.setter
    def id_rol(self, value):
        self._id_rol = value

    @property
    def codigo_usuario(self):
        return self._codigo_usuario

    @codigo_usuario.setter
    def codigo_usuario(self, value):
        self._codigo_usuario = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, value):
        self._apellido = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, value):
        self._telefono = value

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, value):
        self._direccion = value

    @property
    def fecha_registro(self):
        return self._fecha_registro

    @fecha_registro.setter
    def fecha_registro(self, value):
        self._fecha_registro = value

    @property
    def fecha_expiracion(self):
        return self._fecha_expiracion

    @fecha_expiracion.setter
    def fecha_expiracion(self, value):
        self._fecha_expiracion = value

    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, value):
        self._activo = value

    def __str__(self):
        return f"Usuario({self._codigo_usuario}, {self._nombre} {self._apellido})"
