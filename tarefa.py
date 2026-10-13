lista_tarefas = []
id = 1

class Tarefa:
    def __init__(self,id, nome, data, inicio, fim):

        self.id = id
        self.nome = nome
        self.data = data
        self.inicio = inicio
        self.fim = fim

def create(id):

    nome_tarefa = input('Digite o nome da tarefa: ')

    data_tarefa = input('Qual a data da tarefa: ')

    inicio_tarefa = input("Quando se inicia a tarefa: ")

    fim_tarefa = input("Qual a previsão de fim da tarefa: ")

    tarefa = Tarefa(id, nome_tarefa, data_tarefa, inicio_tarefa, fim_tarefa)
    lista_tarefas.append(tarefa)
    id += 1
    return id

id = create(id)

while True:

        escolha = input("Deseja cadastrar uma nova tarefa? [S/N] ").upper()
        if escolha != "S" and escolha != "N":
            print("Digite um valor valido.")
        elif escolha == "S":
            id = create(id)
        elif escolha == "N":
             break

def read():
    
    for dado in lista_tarefas:
        print(f"ID: {dado.id} \n Nome da tarefa: {dado.nome}\n Data da Tarefa: {dado.data}\n Inicio: {dado.inicio}\n Fim: {dado.fim}")

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
        print("Tarefa não encontrada.")

delete()






