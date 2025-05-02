from Entidades.UsuarioSistema import UsuarioSistema
from Dtos.UsuarioSistemaDTO import UsuarioSistemaDTO

def dto_a_usuario_sistema(dto: UsuarioSistemaDTO) -> UsuarioSistema:
    return UsuarioSistema(dto.id, dto.usuario_id, dto.username_payload, None, None, dto.rol_id, None)

def usuario_sistema_a_dto(usuario: UsuarioSistema) -> UsuarioSistemaDTO:
    return UsuarioSistemaDTO(usuario.id, usuario.usuario_id, usuario.username_payload, usuario.contrasena, usuario.rol_id)

def fila_a_usuario_sistema(fila: tuple) -> UsuarioSistema:
    return UsuarioSistema(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])