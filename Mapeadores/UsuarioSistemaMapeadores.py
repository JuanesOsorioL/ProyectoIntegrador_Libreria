from Entidades.UsuarioSistema import UsuarioSistema
from Dtos.UsuarioSistemaDTO import UsuarioSistemaDTO

def dto_a_usuario_sistema(dto: UsuarioSistemaDTO) -> UsuarioSistema:
    return UsuarioSistema(dto.get_id(), dto.get_usuario_id(), dto.get_nombre_usuario(), None, dto.get_contrasena(), None)

def usuario_sistema_a_dto(usuario: UsuarioSistema) -> UsuarioSistemaDTO:
    return UsuarioSistemaDTO(usuario.Get_Id(), usuario.Get_UsuarioId(), usuario.Get_nombre_usuario(), usuario.Get_Contrasena(), None)

def usuario_sistema_a_dto(usuario: UsuarioSistema,nombre_usuario) -> UsuarioSistemaDTO:
    return UsuarioSistemaDTO(usuario.Get_Id(), usuario.Get_UsuarioId(), nombre_usuario, usuario.Get_Contrasena(), None)

def fila_a_usuario_sistema(fila: tuple) -> UsuarioSistema:
    return UsuarioSistema(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])

def fila_a_usuario_sistema_dto(fila: tuple) -> UsuarioSistemaDTO:
    return UsuarioSistemaDTO(fila[0],fila[1],fila[2],fila[4],fila[6])