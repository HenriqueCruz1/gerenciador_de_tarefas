lista_tarefas = []

class Tarefa:
    def __init__(self, nome, data, inicio, fim):

        self.nome = nome
        self.data = data
        self.inicio = inicio
        self.fim = fim

def create():

    nome_tarefa = input('Digite o nome da tarefa: ')

    data_tarefa = input('Qual a data da tarefa: ')

    inicio_tarefa = input("Quando se inicia a tarefa: ")

    fim_tarefa = input("Qual a previsão de fim da tarefa: ")

    tarefa = Tarefa(nome_tarefa, data_tarefa, inicio_tarefa, fim_tarefa)
    lista_tarefas.append(tarefa)

create()

def read():
    for dado in lista_tarefas:
        print(dado.nome, dado.data, dado.inicio, dado.fim)

read()

def update():
    encontrado = False
    busca_tarefa = input("Busque pelo nome da tarefa para alterar: ")

    for dado in lista_tarefas:
        if dado.nome == busca_tarefa:
            encontrado = True
            novo_nome = input("Digite o novo nome da tarefa: ")
            dado.nome = novo_nome
            nova_data = input("Digite a nova data: ")
            dado.data = nova_data
            novo_inicio = input("Digite o novo inicio: ")
            dado.inicio = novo_inicio
            novo_fim = input("Digite o novo fim previsto: ")
            dado.fim = novo_fim
    if encontrado == False:
        print("Tarefa não encontrada")
    else:
        print("Atualização feita com sucesso")

update()

def delete():

    encontrado = False
    busca = input("Digite a tarefa que deseja deletar: ")
    for dado in lista_tarefas:
        if dado.nome == busca:
            encontrado = True
            lista_tarefas.remove(dado)      
    if encontrado == False:
        print("Usuario não encontrado.")

delete()






