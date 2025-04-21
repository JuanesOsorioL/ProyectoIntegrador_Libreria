from Entidades.Usuario import Usuario
from Dtos.UsuarioDTO import UsuarioDTO

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


#def fila_a_usuario_sistema(fila: tuple) -> UsuarioSistema:
  #  return UsuarioSistema(id=fila[0], usuario_id=fila[1], username=fila[2], password_hash=fila[3])