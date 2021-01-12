#________inicializar sistema__________
print("Bem-Vindo(a) ao sistema da biblioteca")
nomeUsuario = str(input("Digite o seu nome completo: "))

#_________inserindo classes____________
class Livro:
    def __init__(self, numero, titulo, autor, ano, status,):
        self.numero = numero
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.status = status
        self.emprestado = ''

    def addEmprestado(self, usuario):
        self.emprestado = usuario

    def statusDis(self):
        self.status = 'Disponível'

    def statusInds(self):
        self.status = 'Indisponível'

#_________Definindo livros primarios_________
livros = [Livro(1, 'Código Limpo', 'Tio Bob', 2001, 'Disponível'), Livro(2, 'Como fazer sentido e bater o martelo? ', 'Alexandro Aolchique', 2017, 'Disponível'), Livro(3, 'Basquete 101', 'Hortência Marcari', 2010, 'Disponível')]

#_________definindo funções___________
def menuIniciar():
    op = 0

    while op != 4:
        print('\n')
        print('''---Menu de entrada---
    [1] Retirar um livro
    [2] Devolver um livro
    [3] Doar um livro
    [4] Sair''')
        op = int(input("Digite sua opção: "))
        print("--"*14)
        return op

def menulivros():
    print('\n')
    mostraLivros = len(livros)

    for x in range(0,mostraLivros):
        print(f'[{x + 1}] {livros[x].titulo}')
    return int(input('Selecione 0 para voltar ou o numero do livro desejado: '))

def menuDevolveLivro():
    print('\n')
    mostraLivros = len(livros)

    temlivro = False

    for x in range(0,mostraLivros):
        if livros[x].emprestado != '' and livros[x].emprestado == nomeUsuario:
            print(f'[{x + 1}] {livros[x].titulo}')
            temlivro = True

    if temlivro:
        return int(input('Selecione 0 para voltar ou o numero do livro desejado: '))
    else:
        return 0

def constroiLivro(nume):
    print('\n')
    print(f'''----Livro selecionado----
    Numero: {livros[nume].numero}
    Titulo: {livros[nume].titulo}    
    Autor: {livros[nume].autor}
    Ano: {livros[nume].ano}
    Status: {livros[nume].status}
    Emprestado para: {livros[nume].emprestado}''')

def addLivro():
    number = len(livros) + 1

    escolha = 0
    while escolha == 0:
        tittle = str(input("Digite o nome do livro: "))
        dono = str(input("Digite o autor do livro: "))
        idade = int(input("Digite o ano de publicação do livro: "))

        print(f'''----Livro a ser doado----
    Numero: {number}
    Titulo: {tittle}    
    Autor: {dono}
    Ano: {idade}''')
        dados = int(input('Digite 0 para alterar os dados e 1 para salvar: '))
        if dados == 1:
            escolha = 1

    livros.append(Livro(number, tittle, dono, idade, 'Disponível'))
    return


#_________rodando o sistema da biblioteca_________
online = True

while online == True:
    op = menuIniciar()
    if op == 1:
        escolha = menulivros()

        mostraLivros = len(livros)

        if escolha == 0:
            print('Bem-Vindo(a) de volta ao menu iniciar')
        elif escolha > 0 and escolha <= mostraLivros:
            constroiLivro(escolha - 1)
            if livros[escolha - 1].emprestado == '':
                pega = int(input('Digite 0 para voltar ao menu principal e 1 para retirar: '))
                if pega == 1:
                    print('Obrigado pela escolha. Tenha uma boa leitura :).')
                    livros[escolha - 1].addEmprestado(nomeUsuario)
                    livros[escolha - 1].statusInds()
                else:
                    print('Bem-Vindo(a) de volta ao menu iniciar')
            else:
                print('Livro ja foi retirado :(. Mas não se preocupe em breve ele estara de volta :).')
        else:
            print('Livro não encontrado.....')
            print('Bem-Vindo(a) de volta ao menu iniciar')
                
    elif op == 2:
        escolha = menuDevolveLivro()

        mostraLivros = len(livros)

        if escolha == 0:
            print('Bem-Vindo(a) de volta ao menu iniciar')
        elif escolha > 0 and escolha <= mostraLivros:
            if livros[escolha - 1].emprestado != '':
                constroiLivro(escolha - 1)
                pega = int(input('Digite 0 para voltar ao menu principal e 1 confirmar: '))
                if pega == 1:
                    print('Devolução concluida :). Confira os outros livros disponiveis na biblioteca.')
                    livros[escolha - 1].addEmprestado('')
                    livros[escolha - 1].statusDis()
                else:
                    print('Bem-Vindo(a) de volta ao menu iniciar')
            else:
                print('Livro não encontrado...')
        else:
            print('Livro não encontrado.....')
            print('Bem-Vindo(a) de volta ao menu iniciar')

    elif op == 3:
        escolha = int(input("Digite 0 para voltar e 1 para continuar: "))
        if escolha == 0:
            print('Bem-Vindo(a) de volta ao menu iniciar')
        elif escolha == 1:
            addLivro()
            print('Livro adicionado ao sistema. Obrigado pela doação :).')
        else:
            print("Opção não encontrada...")
    elif op == 4:
        online = False
        print("Finalizando o programa...")
    else:
        print("Opção invalida. Por favor, digite um numero novamente.")
    print("--"*14)

print("Obrigado por acessar a biblioteca")