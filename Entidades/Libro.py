class Libro:
    def __init__(self, id=None, titulo="", isbn="", descripcion="", anio_publicacion=None,
                 formato="", editorial_id=None, precio=0.0, stock=0):
        self.id = id
        self.titulo = titulo
        self.isbn = isbn
        self.descripcion = descripcion
        self.anio_publicacion = anio_publicacion
        self.formato = formato
        self.editorial_id = editorial_id
        self.precio = precio
        self.stock = stock
