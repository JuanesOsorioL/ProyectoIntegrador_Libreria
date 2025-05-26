from Entidades.Rol import Rol
from Dtos.RolDTO import RolDTO











from Entidades.Libro import Libro
from Dtos.LibroDTO import LibroDTO

from Entidades.Venta import Venta
from Dtos.VentaDTO import VentaDTO

from Entidades.DetalleVenta import DetalleVenta
from Dtos.DetalleVentaDTO import DetalleVentaDTO

from Entidades.Prestamo import Prestamo
from Dtos.PrestamoDTO import PrestamoDTO

from Entidades.DetallePrestamo import DetallePrestamo
from Dtos.DetallePrestamoDTO import DetallePrestamoDTO


"""Mapeador Rol"""
def rol_a_dto(rol: Rol) -> RolDTO:
    return RolDTO(id=rol.id, nombre=rol.nombre)

def dto_a_rol(rol_dto: RolDTO) -> Rol:
    return Rol(id=rol_dto.id, nombre=rol_dto.nombre)

def fila_a_rol(fila: tuple) -> Rol:
    return Rol(id=fila[0], nombre=fila[1])

"""Mapeador Editorial"""



"""Mapeador Autor"""



"""Mapeador Categoria"""



"""Mapeador LibroCategoria"""



"""Mapeador LibroAutor"""



"""Mapeador Devolucion"""



"""Mapeador Libro"""

def libro_a_dto(libro: Libro) -> LibroDTO:
    return LibroDTO(
        id=libro.id,
        titulo=libro.titulo,
        isbn=libro.isbn,
        descripcion=libro.descripcion,
        anio_publicacion=libro.anio_publicacion,
        formato=libro.formato,
        editorial_id=libro.editorial_id,
        precio=libro.precio,
        stock=libro.stock
    )

def dto_a_libro(dto: LibroDTO) -> Libro:
    return Libro(
        id=dto.id,
        titulo=dto.titulo,
        isbn=dto.isbn,
        descripcion=dto.descripcion,
        anio_publicacion=dto.anio_publicacion,
        formato=dto.formato,
        editorial_id=dto.editorial_id,
        precio=dto.precio,
        stock=dto.stock
    )

def fila_a_libro(fila: tuple) -> Libro:
    return Libro(*fila)

# Ventas

def venta_a_dto(venta: Venta) -> VentaDTO:
    return VentaDTO(
        id=venta.id,
        usuario_id=venta.usuario_id,
        empleado_id=venta.empleado_id,
        fecha=venta.fecha,
        total=venta.total
    )

def dto_a_venta(dto: VentaDTO) -> Venta:
    return Venta(
        id=dto.id,
        usuario_id=dto.usuario_id,
        empleado_id=dto.empleado_id,
        fecha=dto.fecha,
        total=dto.total
    )

def fila_a_venta(fila: tuple) -> Venta:
    return Venta(*fila)

# Detalle Venta

def detalle_venta_a_dto(entidad: DetalleVenta) -> DetalleVentaDTO:
    return DetalleVentaDTO(
        venta_id=entidad.venta_id,
        libro_id=entidad.libro_id,
        cantidad=entidad.cantidad,
        precio_unitario=entidad.precio_unitario
    )

def dto_a_detalle_venta(dto: DetalleVentaDTO) -> DetalleVenta:
    return DetalleVenta(
        venta_id=dto.venta_id,
        libro_id=dto.libro_id,
        cantidad=dto.cantidad,
        precio_unitario=dto.precio_unitario
    )

def fila_a_detalle_venta(fila: tuple) -> DetalleVenta:
    return DetalleVenta(
        venta_id=fila[0],
        libro_id=fila[1],
        cantidad=fila[2],
        precio_unitario=float(fila[3])  # subtotal se recalcula automáticamente
    )

#Prestamo

def prestamo_a_dto(entidad: Prestamo) -> PrestamoDTO:
    return PrestamoDTO(
        id=entidad.id,
        usuario_id=entidad.usuario_id,
        empleado_id=entidad.empleado_id,
        fecha_prestamo=entidad.fecha_prestamo,
        fecha_devolucion=entidad.fecha_devolucion,
        estado=entidad.estado
    )

def dto_a_prestamo(dto: PrestamoDTO) -> Prestamo:
    return Prestamo(
        id=dto.id,
        usuario_id=dto.usuario_id,
        empleado_id=dto.empleado_id,
        fecha_prestamo=dto.fecha_prestamo,
        fecha_devolucion=dto.fecha_devolucion,
        estado=dto.estado
    )

def fila_a_prestamo(fila: tuple) -> Prestamo:
    return Prestamo(*fila)

# Detalle Prestamo

def detalle_prestamo_a_dto(entidad: DetallePrestamo) -> DetallePrestamoDTO:
    return DetallePrestamoDTO(
        prestamo_id=entidad.prestamo_id,
        libro_id=entidad.libro_id,
        cantidad=entidad.cantidad
    )

def dto_a_detalle_prestamo(dto: DetallePrestamoDTO) -> DetallePrestamo:
    return DetallePrestamo(
        prestamo_id=dto.prestamo_id,
        libro_id=dto.libro_id,
        cantidad=dto.cantidad
    )

def fila_a_detalle_prestamo(fila: tuple) -> DetallePrestamo:
    return DetallePrestamo(
        prestamo_id=fila[0],
        libro_id=fila[1],
        cantidad=fila[2]
    )



