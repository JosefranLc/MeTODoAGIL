alunos = [] #Lista de alunos, cada aluno será armazenado dentro dela.

def menu(): #Função do menu
    while True: #Loop infinito
        print("\n===== SISTEMA ESCOLAR =====") # Mostra o menu de opções para o usuário
        print("1 - Cadastrar aluno")
        print("2 - Registrar nota")
        print("3 - Registrar frequência")
        print("4 - Ver status do aluno")
        print("5 - Listar alunos")
        print("6 - Sair")

        # input captura o que o usuário digitar, basicamente o menu de escolha das opções anteriores.
        op = input("Escolha: ")

        # OPÇÃO 1 - CADASTRAR ALUNO
        if op == "1":
            nome = input("Nome do aluno: ") #aqui pede o nome do aluno
            matricula = input("Matrícula: ") #aqui pede a matricula do aluno

            # criamos um dicionário com os dados do aluno
            aluno = {
                "nome": nome, # guarda o nome
                "matricula": matricula, # guarda a matrícula
                "notas": [], # lista vazia para guardar notas
                "frequencia": 0 # frequência começa em 0
            }

            alunos.append(aluno) # adiciona o aluno dentro da lista alunos
            print("Aluno cadastrado!") #mensagem de confirmação

        # OPÇÃO 2 - REGISTRAR NOTA
        elif op == "2":
            matricula = input("Matrícula do aluno: ") #aqui pede a matricula do aluno

            for aluno in alunos: # percorre toda a lista de alunos a procuda do mesmo
                if aluno["matricula"] == matricula: # verifica se a matrícula digitada é igual à do aluno
                    nota = float(input("Digite a nota: ")) # pede a nota

                    aluno["notas"].append(nota) # adiciona a nota dentro da lista de notas
                    print("Nota adicionada!") #mensagem de confirmação

        # OPÇÃO 3 - REGISTRAR FREQUÊNCIA
        elif op == "3":
            matricula = input("Matrícula do aluno: ")

            for aluno in alunos: # percorre a lista de alunos igual a opção 2
                if aluno["matricula"] == matricula: # verifica se é o mesmo aluno digitado 
                    freq = float(input("Digite a frequência (%): ")) # digitamos a frequencia dele em numeros
                    aluno["frequencia"] = freq # salva a frequencia no dicionário
                    print("Frequência registrada!") #mensagem de confirmação

        # OPÇÃO 4 - VER STATUS DO ALUNO
        elif op == "4":
            matricula = input("Matrícula do aluno: ") #aqui pede a matricula do aluno

            for aluno in alunos: #denovo percorremos a lista de alunos
                if aluno["matricula"] == matricula: #vemos se é o mesmo aluno digitado

                    if len(aluno["notas"]) > 0: #verifica se o aluno tem notas registradas, len explicado abaixo
                        media = sum(aluno["notas"]) / len(aluno["notas"]) #sum soma todas as notas, len conta quantas notas existem
                        # calculandoa assim a média dividindo soma pela quantidade
                    else:
                        media = 0 #se não tem notas, não tem resultado

                    freq = aluno["frequencia"] # pega a frequência do aluno

                    if media >= 70 and freq >= 75: # se média for maior ou igual a 70 e frequência maior ou igual a 75 → aprovado
                        status = "Aprovado"
                    elif 40 <= media < 70:  # se média está entre 40 e 69 → reforço
                        status = "Reforço"
                    else:  # caso contrário → reprovado
                        status = "Reprovado"
 
                    # mostra os resultados do aluno
                    print("\nAluno:", aluno["nome"])
                    print(f"Média: {media:.2f}") # a media vai aperecer apenas com 2 casas decimais com o :.2f
                    print("Frequência:", freq,"%")
                    print("Status:", status)

        # OPÇÃO 5 - LISTAR ALUNOS
        elif op == "5": 
            print("\nLista de alunos:")
            for aluno in alunos: #denovos vemos os alunos dentro da lista
                print(aluno["nome"], "-", aluno["matricula"]) # e mostra nome e matrícula dos alunos

        # OPÇÃO 6 - SAIR
        elif op == "6":
            break #aqui encerramos o "sistema de notas"

        else:
            print("Opção inválida") #aqui é quando digitam alguma coisa diferente de 1,2,3,4,5 e 6

# chama a função menu para iniciar o programa, se escolhemos alguma opção além do 6 ele fica repetindo
menu()
