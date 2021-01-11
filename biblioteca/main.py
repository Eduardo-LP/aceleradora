#________inicializar sistema__________
print("Bem-Vindo(a) ao sistema da biblioteca")
nomeUsuario = str(input("Digite o seu nome completo: "))
print("=-"*14)

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

#_________Definindo livros primarios_________
livros = [Livro(1, 'Código Limpo', 'Tio Bob', 2001, 'Disponível'), Livro(2, 'Como fazer sentido e bater o martelo? ', 'Alexandro Aolchique', 2017, 'Disponível'), Livro(3, 'Basquete 101', 'Hortência Marcari', 2010, 'Disponível')]

#_________definindo funções___________
def menuIniciar():
    op = 0

    while op != 4:
        print('''---Menu de entrada---
    [1] Retirar um livro
    [2] Devolver um livro
    [3] Doar um livro
    [4] Sair''')
        op = int(input("Digite sua opção: "))
        print("--"*14)
        return op

def menulivros():
    mostraLivros = len(livros)

    for x in range(0,mostraLivros):
        print(f'[{x + 1}] {livros[x].titulo}')
    return int(input('Selecione 0 para voltar ou o numero do livro desejado: '))

def menuDevolveLivros():
    mostraLivros = len(livros)

    for x in range(0,mostraLivros):
        if livros[x].emprestado != '':
            print(f'[{x + 1}] {livros[x].titulo}')
    return int(input('Selecione 0 para voltar ou o numero do livro desejado: '))


def constroiLivro(nume):
    print(f'''----Livro selecionado----
    Numero: {livros[nume].numero}
    Titulo: {livros[nume].titulo}    
    Autor: {livros[nume].autor}
    Ano: {livros[nume].ano}
    Status: {livros[nume].status}
    Emprestado para: {livros[nume].emprestado}''')

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
            if livros[escolha].emprestado == '':
                pega = int(input('Digite 0 para retirar e 1 para voltar ao menu principal: '))
                if pega == 0:
                    print('Obrigado pela escolha. Tenha uma boa leitura :).')
                    livros[escolha].addEmprestado(nomeUsuario)
                else:
                    print('Bem-Vindo(a) de volta ao menu iniciar')
            else:
                print('Livro ja foi retirado :(. Mas não se preocupe em breve ele estara de volta :).')
        else:
            print('Livro não encontrado.....')
            print('Bem-Vindo(a) de volta ao menu iniciar')
                
    elif op == 2:
        escolha = menuDevolveLivros()

        mostraLivros = len(livros)

        if escolha == 0:
            print('Bem-Vindo(a) de volta ao menu iniciar')
        elif escolha > 0 and escolha <= mostraLivros:
            if livros[escolha].emprestado != '':
                constroiLivro(escolha - 1)
                devolve = int(input('Digite 0 para confirmar e 1 para voltar ao menu principal: '))
                if devolve == 0:
                    print('Obrigado pela escolha :). Fique a vontade para escolher outros livros.')
                    livros[escolha].addEmprestado('')
                else:
                    print('Bem-Vindo(a) de volta ao menu iniciar')
            else:
                print('Este livro esta disponível para retirada')
        else:
            print('Livro não encontrado.....')
            print('Bem-Vindo(a) de volta ao menu iniciar')

    elif op == 3:
        print("op = 3")
    elif op == 4:
        online = False
        print("Finalizando o programa...")
    else:
        print("Opção invalida. Por favor, digite um numero novamente.")
    print("--"*14)

print("Obrigado por acessar a biblioteca")