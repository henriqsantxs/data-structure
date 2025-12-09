filaprofessores = []
filaalunos = []
filavistante = []
filafinal = []
controle = 0

while True:
    print("\n==================================")
    print("   SISTEMA DE ENTRADA NO LABORATORIO")
    print("====================================")
    print("1-Professor")
    print("2-Alunos regulares")
    print("3-Visitante")
    print("4-Processar fila")
    print("5-Exibir filas")
    print("6- Exiir historico de entrada no laboratorio")
    print("7-Finalizar programa")
    op = int(input("Escolha a opção: "))

    if op == 1:
        nome = input ("Nome professor: ")
        filaprofessores.append(nome)
        print(f"Professor {nome} Adicionado")
    elif op == 2:
        nome = input ("Nome aluno regular: ")
        filaalunos.append(nome)
        print(f"Aluno {nome} Adicionado")
    elif op == 3:
        nome = input ("Nome Visitante: ")
        filavistante.append(nome)
    elif op == 4: 
        if not filaalunos and not filaprofessores and not filavistante:
            print("Filas sem processamentos(Filas vazias).")
        elif filaalunos and filaprofessores and filavistante and controle == 0:
            pessoa = filaprofessores.pop(0)
            filafinal.append(pessoa)
            print(f"Professor {pessoa} entrou no Laboratorio.")
            controle = 1
        elif filaalunos and filaprofessores and filavistante and controle == 1:
            pessoa = filaalunos.pop(0)
            filafinal.append(pessoa)
            print(f"Aluno {pessoa} entrou no Laboratorio.")
            controle = 2

        elif filaalunos and filaprofessores and filavistante and controle == 2:
            pessoa = filavistante.pop(0)
            filafinal.append(pessoa)
            print(f"Visitante {pessoa} entrou no Laboratorio.")
            controle = 0

        elif filaalunos and filaprofessores and not filavistante and controle == 0:
            pessoa = filaprofessores.pop(0)
            filafinal.append(pessoa)
            print(f"Professor {pessoa} entrou no laboratorio")
            controle = 1

        elif filaalunos and filaprofessores and not filavistante and controle == 1:
            pessoa = filaalunos.pop(0)
            filafinal.append(pessoa)
            print(f"Aluno {pessoa} entrou no laboratorio")
            controle = 0

        elif filavistante and filaprofessores and not filaalunos and controle == 0:
            pessoa = filaprofessores.pop(0)
            filafinal.append(pessoa)
            print(f"Professor {pessoa} entrou no laboratorio")
            controle = 2

        elif filavistante and filaprofessores and not filaalunos and controle == 2:
            pessoa = filavistante.pop(0)
            filafinal.append(pessoa)
            print(f"Visitante {pessoa} entrou no laboratorio")
            controle = 1

        elif filaalunos and filavistante and not filaprofessores and controle == 1:
            pessoa = filaalunos.pop(0)
            filafinal.append(pessoa)
            print(f"Aluno {pessoa} entrou no laboratorio")
            controle = 2
        elif filaalunos and filavistante and not filaprofessores and controle == 2:
            pessoa = filavistante.pop(0)
            filafinal.append(pessoa)
            print(f"Visitante {pessoa} entrou no laboratorio")
            controle = 0

        elif filaprofessores and not filaalunos and not filavistante:
            pessoa = filaprofessores.pop(0)
            filafinal.append(pessoa)
            print(f"Professor {pessoa} entrou no laboratorio")
        
        elif filaalunos and not filaprofessores and not filavistante:
            pessoa = filaalunos.pop(0)
            filafinal.append(pessoa)
            print(f"Aluno {pessoa} entrou no laboratorio")
        
        elif filavistante and not filaprofessores and not filaalunos:
            pessoa = filavistante.pop(0)
            filafinal.append(pessoa)
            print(f"Visitante {pessoa} entrou no laboratorio")
    elif op == 5:
        if not filaalunos and not filaprofessores and not filavistante:
            print("Filas vazias.")
        else:
            print("Fila Professor: ", filaprofessores)
            print("Fila alunos regulares: ", filaalunos)
            print("Fila visitante: ", filavistante)

    elif op == 6:
        if not filafinal:
            print("Historico de entrada vazio")
        else:
            print("Historico de entrada no laboratorio: ", filafinal)

    elif op == 7:
        print("Encerrando programa...")
        break
    else: 
        print("Opção invalida.")
        
    
    

        
        
        
            

