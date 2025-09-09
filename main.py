# Gerenciador de Tarefas (To-Do List)
# Autor: Seu Nome
# Curso: Análise e Desenvolvimento de Sistemas

tarefas = []

def mostrar_menu():
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Sair")

def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    tarefas.append({"tarefa": tarefa, "concluida": False})
    print("✅ Tarefa adicionada com sucesso!")

def listar_tarefas():
    if not tarefas:
        print("⚠️ Nenhuma tarefa cadastrada.")
    else:
        print("\n--- Lista de Tarefas ---")
        for i, t in enumerate(tarefas):
            status = "✅" if t["concluida"] else "❌"
            print(f"{i+1}. {t['tarefa']} - {status}")

def concluir_tarefa():
    listar_tarefas()
    if tarefas:
        indice = int(input("Digite o número da tarefa para concluir: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            print("🎉 Tarefa concluída com sucesso!")
        else:
            print("⚠️ Número inválido.")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        concluir_tarefa()
    elif opcao == "4":
        print("👋 Saindo do programa...")
        break
    else:
        print("⚠️ Opção inválida. Tente novamente.")
