tarefas = []

print("=== TASK MANAGER ===")
print("1 - Adicionar tarefa")
print("2 - Listar tarefas")
print("3 - Sair")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    descricao = input("Digite a descrição da tarefa: ")
    tarefas.append(descricao)
    print("Tarefa adicionada.")
elif opcao == "2":
    print("Lista de tarefas:")
    for tarefa in tarefas:
        print("-", tarefa)
elif opcao == "3":
    print("Saindo...")
else:
    print("Opção inválida.")