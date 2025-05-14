from Entidades.Usuario import Usuario
from Entidades.Rol import Rol
from Dtos.UsuarioDTO import UsuarioDTO
from Dtos.RolDTO import RolDTO

def dto_a_usuario(dto: UsuarioDTO,datos:dict) -> Usuario:
    return Usuario(None,
                   datos["nombre"],
                   datos["nombre_hmac"],
                   datos["email"],
                   datos["email_hmac"],
                   datos["telefono"],
                   datos["telefono_hmac"],
                   datos["direccion"],
                   datos["direccion_hmac"],
                   None,
                   dto.Get_RolId(),
                   None)

def usuario_a_dto(usuario: Usuario,rol:RolDTO) -> UsuarioDTO:
    return UsuarioDTO(usuario.Get_Id(),usuario.Get_Nombre(),usuario.Get_Email(),usuario.Get_Telefono(),usuario.Get_Direccion(),usuario.Get_FechaRegistro(),usuario.Get_RolId(),rol)


def fila_a_usuario(fila: tuple) -> Usuario:
    return Usuario(*fila)






    """


     
        
       
        

    def usuario_a_dto(usuario: Usuario) -> UsuarioDTO:
        return UsuarioDTO(
            id=usuario.id,
            nombre=usuario.nombre,
            email=usuario.email,
            telefono=usuario.telefono,
            direccion=usuario.direccion,
            fechaRegistro=usuario.fechaRegistro,
            rolId=usuario.rolId
        )

    def dto_a_usuario(dto: UsuarioDTO) -> Usuario:
        return Usuario(
            id=dto.id,
            nombre=dto.nombre,
            email=dto.email,
            telefono=dto.telefono,
            direccion=dto.direccion,
            fechaRegistro=dto.fechaRegistro,
            rolId=dto.rolId
        )

    def fila_a_usuario(fila: tuple) -> Usuario:
        return Usuario(*fila)

    """





#def fila_a_usuario_sistema(fila: tuple) -> UsuarioSistema:
  #  return UsuarioSistema(id=fila[0], usuario_id=fila[1], username=fila[2], password_hash=fila[3])