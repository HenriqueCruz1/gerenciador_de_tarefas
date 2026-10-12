lista_de_usuarios = []

class Usuario:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

def create():

    nome = input('Digite o nome do usuario: ')

    idade = int(input('Digite a idade do usuario: '))

    usuario = Usuario(nome, idade)
    lista_de_usuarios.append(usuario)


create()


def read():
    encontrado = False
    busca = input("Digite o usuario que deseja buscar: ")
    for dado in lista_de_usuarios:
        if dado.nome == busca:
            encontrado = True
            print(dado.nome, dado.idade)
    if encontrado == False:
        print("Usuario não encontrado.")

read()


def update():
    encontrado = False
    nome = input("Digite o nome do usuario que deseja alterar: ")
    for dado in lista_de_usuarios:
        if nome == dado.nome:
            encontrado = True
            nome_alterado = input("Digite o novo nome do usuario: ")
            dado.nome = nome_alterado
            while True:
                escolha = input("Deseja alterar a idade?[S/N] ").upper()
                if escolha != "S" and escolha != "N":
                    print("Entrada invalida!")
                elif escolha == "S":
                    idade_alterada = int(input("Digite a nova idade do usuario: "))
                    dado.idade = idade_alterada
                    break
                else:
                    break
    if encontrado == False:
        print("Usuario não encontrado.")
    else:
        print("Atualização feita com sucesso!")

update()


def delete():
    encontrado = False
    busca = input("Digite o usuario que deseja deletar: ")
    for dado in lista_de_usuarios:
        if dado.nome == busca:
            encontrado = True
            lista_de_usuarios.remove(dado)      
    if encontrado == False:
        print("Usuario não encontrado.")

delete()