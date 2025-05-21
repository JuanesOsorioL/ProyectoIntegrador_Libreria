from Entidades.Usuario import Usuario
from Dtos.UsuarioDTO import UsuarioDTO
from Dtos.RolDTO import RolDTO

def dto_a_usuario_dos(dto: UsuarioDTO,datos:dict) -> Usuario:
    return Usuario(dto.Get_Id(),datos["nombre"],datos["nombre_hmac"],datos["email"],datos["email_hmac"],datos["telefono"],
                   datos["telefono_hmac"],datos["direccion"],datos["direccion_hmac"],dto.Get_FechaRegistro(),dto.Get_RolId(),None)

def dto_a_usuario(dto: UsuarioDTO) -> Usuario:
    return Usuario(dto.Get_Id(),dto.Get_Nombre(),None,dto.Get_Email(),None,dto.Get_Telefono(),None,dto.Get_Direccion(),None,dto.Get_FechaRegistro(),dto.Get_RolId(),None)

def usuario_a_dto_dos(usuario: Usuario, rol:RolDTO) -> UsuarioDTO:
    return UsuarioDTO(usuario.Get_Id(),usuario.Get_Nombre(),usuario.Get_Email(),usuario.Get_Telefono(),usuario.Get_Direccion(),usuario.Get_FechaRegistro(),usuario.Get_RolId(),rol)

def usuario_a_dto(usuario: Usuario) -> UsuarioDTO:
    return UsuarioDTO(usuario.Get_Id(),usuario.Get_Nombre(),usuario.Get_Email(),usuario.Get_Telefono(),usuario.Get_Direccion(),usuario.Get_FechaRegistro(),usuario.Get_RolId(),None)

def fila_a_usuario(fila: tuple) -> Usuario:
    return Usuario(*fila)

def fila_a_usuario_only_rolID(fila: tuple) -> Usuario:
    return Usuario(None,None,None,None,None,None,None,None,None,None,fila[6],None)