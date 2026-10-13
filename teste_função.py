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
        for dado in lista_tarefas:
            print(f"ID: {dado.id} \n Nome da tarefa: {dado.nome}\n Data da Tarefa: {dado.data}\n Inicio: {dado.inicio}\n Fim: {dado.fim}")
        break
    