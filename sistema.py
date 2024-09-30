alunos = list()

while True:
    print ("SISTEMA ACADÊMICO")
    print ('''Escolha uma opção:
    1-Adicionar nome do aluno
    2-Editar informações de nome de aluno
    3-Excluir aluno existente       
    4-Adição de notas do aluno
    5-Frequência do aluno
    6-Relatório de situação do aluno''')
    opcoes = str(input())
    
    if opcoes == "1":
        qtd_aluno = int(input("Quantos alunos você quer inserir? "))
        cont = 0 
        while cont < qtd_aluno:
            nome = (str(input("Nome do aluno: ")))
            alunos.append({"nome":nome, "nota":[], "media":0.0, "frequencia":0})
            cont+=1
        print(alunos)

    elif opcoes == "2":
        print("Lista dos alunos")
        for i, aluno in enumerate(alunos):
            print(f"{i}.{aluno}")
        nome_antigo = int(input("Selecione o número correspondente ao aluno que você deseja editar: "))
        
        if nome_antigo > len(alunos): 
            print("Este nome não existe! Escolha um número existente.")
        else:
            nome_novo = str(input("Qual o novo nome? "))
            alunos[nome_antigo]["nome"]=nome_novo
        print(alunos)

    elif opcoes == "3":
        print("Lista dos alunos")
        for i, aluno in enumerate(alunos):
            print(f'{i}.{aluno}') 
        aluno_a_ser_excluido = int(input("Digite o número correspondente ao aluno que deseja excluir: "))  

        if aluno_a_ser_excluido > len(alunos):
            print("Este número não está na lista! Indique um número existente: ")
        
        else:
            del(alunos[aluno_a_ser_excluido])
        print(alunos)


    elif opcoes == "4":
        print("Lista dos alunos")
        for i, aluno in enumerate(alunos):
            print(f"{i}.{aluno}")

        indice = int(input("Selecione o número correspondente ao aluno que você deseja inserir nota: "))
        if indice <= len(alunos): 
            
            notas = list()
            cont = 1
            while cont <= 4:
                nota_aluno = float(input(f"Insira a nota {cont} ou use '-1' para parar o programa: "))
                cont+=1
                if nota_aluno == -1: 
                    break
                notas.append(nota_aluno)
            print(notas)  
            alunos[indice]["nota"] = notas
            media = sum(notas)/len(notas) 
            alunos[indice]["media"] = media
            print(alunos)
    
    elif opcoes == "5": 
        print("Lista dos alunos")
        for i, aluno in enumerate(alunos):
            print(f"{i}.{aluno}")
        frequencia_alunos = int(input("Selecione o número que corresponde ao aluno desejado: "))

        if frequencia_alunos <= len(alunos):
            c_horaria = int(input("Insira a carga horária do curso (Digite apenas números): "))
            frequencia = int(input("Digite a frequência do aluno (Em horas/aula): "))
            porcent = frequencia / c_horaria * 100
        alunos[frequencia_alunos]["frequencia"] = porcent
        print(alunos)

    elif opcoes == "6":
       
        print("Relatório dos Alunos")
        for aluno in alunos: 
            if aluno["media"]<7 and aluno["frequencia"]<75:
                situacao = ("Aluno reprovado por média e falta")

            elif aluno["media"]<7 and aluno["frequencia"]>=75:
                situacao = ("Aluno reprovado por média")

            elif aluno["media"] and aluno["frequencia"]<75:  
                situacao = ("Aluno reprovado por falta")  

            elif aluno["media"]>=7 and aluno["frequencia"]>=75:
               situacao = ("Aluno aprovado por média e frequência")

            opcao_situacao = str(input('''Qual relatório você deseja consultar?
            -Aluno reprovado por média e falta
            -Aluno reprovado por média
            -Aluno reprovado por falta
            -Aluno aprovado por média e frequência
            '''))

            if situacao == opcao_situacao:
                print(f"{aluno['nome']} - Média: {aluno['media']:.2f} - Frequência: {aluno['frequencia']}% - Situação: {situacao}")
            
            else: 
                break 
  
