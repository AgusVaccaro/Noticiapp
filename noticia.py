class Noticia:
    def __init__(self, titulo, descripcion, enlace):
        self.titulo = titulo
        self.descripcion = descripcion
        self.enlace = enlace

    def __str__(self):
        return self.titulo
