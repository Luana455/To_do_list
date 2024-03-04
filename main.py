class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self):
        tarefa = input("Digite a tarefa que deseja adicionar (ou 'menu' para voltar ao menu): ")
        if tarefa.lower() == 'menu':
            return
        self.tarefas.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada com sucesso.")
        self.exibir_menu()

    def listar_tarefas(self):
        if self.tarefas:
            print("Lista de Tarefas:")
            for tarefa in self.tarefas:
                print("-", tarefa)
        else:
            print("Não há tarefas a serem exibidas.")

    def exibir_menu(self):
        while True:
            print("MENU:")
            print("1- Adicionar Tarefa")
            print("2- Ver Tarefas")
            print("0- Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.adicionar_tarefa()
            elif opcao == "2":
                self.listar_tarefas()
            elif opcao == "0":
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Por favor, escolha novamente.")


gerenciador = GerenciadorDeTarefas()
gerenciador.exibir_menu()