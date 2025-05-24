class LibroDTO:
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

    def __str__(self):
        return (f"Id={self.id}, Titulo='{self.titulo}', ISBN='{self.isbn}', Año={self.anio_publicacion}, "
                f"Formato='{self.formato}', Editorial={self.editorial_id}, Precio={self.precio}, Stock={self.stock}")
