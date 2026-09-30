class Post:
    def __init__(self, autor, curtidas, comentarios, descricao):
        self.autor = autor
        self.curtidas = curtidas
        self.comentarios = comentarios
        self.descricao = descricao
    def curtir(self):
        self.curtidas += 1
    def descurtir(self):
        self.curtidas -= 1
    