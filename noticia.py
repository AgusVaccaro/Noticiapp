class Noticia:
    def __init__(self, titulo, description, enlace, content):
        self.titulo = titulo
        self.description = description
        self.content = content
        self.enlace = enlace

    def __str__(self):
        return self.titulo
