def pedir_id():

    while True:

        try:
            id_tarefa = int(input("Digite o ID da tarefa: "))
            return id_tarefa
    
        except ValueError:
            print("Por favor, digite um número válido.")

def mostrar_menu():

    print("================================")
    print("######### TASK MANAGER #########")
    print("================================")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("5 - Sair")
    print("================================")