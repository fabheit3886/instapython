from social import posts
class User:
    def __init__(self, user, username, senha, bio):
        self.user = user
        self.username = username
        self._senha = senha
        self.bio = bio
        self.seguindo = []
        self.seguidores = []
        self.posts = []
        
    def follow(self, usuario):
        self.seguindo.append(usuario)
        usuario.seguidores.append(self)

    def unfollow(self, usuario):
        self.seguindo.remove(usuario)
        usuario.seguidores.remove(self)

    def editar_perfil(self):
        print('Editar perfil\n')
        print('''Escolha a mudança\n
              1. User\n
              2. Biografia\n
              0. Voltar''')
        try:
            escolha = input('> ')
            if escolha not in ['1','2','0']:
                raise ValueError
        except ValueError:
            print('Faça uma escolha válida.')
        else:
            if escolha == '1':
                ch_user = input('Novo User: \n')
                self.user = ch_user
            elif escolha == '2':
                ch_bio = input('Nova biografia: \n')
                self.bio = ch_bio
            elif escolha == '0':
                return
            
    def criar_post(self):
        print('CRIAR POST\n')
        descricao = input('Descrição do post: ')
        novo_post =  Post(
            self,
            0,
            [], 
            descricao
        )
        self.posts.append(novo_post)
        return novo_post
