from tarefas import adicionar_tarefa, listar_tarefas, concluir_tarefa, remover_tarefa
from arquivo import carregar_tarefas

def main():

    tarefas = carregar_tarefas()

    if len(tarefas) > 0:
        proximo_id = tarefas[-1]["id"] + 1
    else:
        proximo_id = 1

    while True:

        print("================================")
        print("######### TASK MANAGER #########")
        print("================================")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("5 - Sair")
        print("================================")

        opcao = input("Escolha uma opção: ")

        print("________________________________")
        if opcao == "1":
            proximo_id= adicionar_tarefa(tarefas, proximo_id)

        elif opcao == "2":
            listar_tarefas(tarefas)

        elif opcao == "3":
            concluir_tarefa(tarefas)

        elif opcao == "4":
            remover_tarefa(tarefas)

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida.\n")

if __name__=="__main__":
    main()