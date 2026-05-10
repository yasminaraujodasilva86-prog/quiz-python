while True:
    acertos = []

    print("\033[35m🎮 Bem-vinda ao Quiz!\033[m")
    perguntas = int(input('Quantas perguntas deseja responder? (5, 10 ou 15?): '))

    # ===================== 5 PERGUNTAS =====================
    if perguntas == 5:

        resposta1 = input('Python é uma linguagem de programação? (sim ou não): ')
        if resposta1.strip().casefold() == 'sim':
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta2 = input('Qual é a única fruta que tem as sementes do lado de fora?: ')
        if resposta2.strip().casefold() == 'morango':
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta3 = input('De qual país é originário o Sushi?: ')
        if resposta3.strip().casefold() in ['japao', 'japão']:
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta4 = input('Qual é o único país que participou de todas as Copas do Mundo?: ')
        if resposta4.strip().casefold() == 'brasil':
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta5 = input('Qual é o maior oceano do planeta?: ')
        if resposta5.strip().casefold() in ['pacifico', 'pacífico']:
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        print(f'\033[33mVocê acertou {len(acertos)} de 5 perguntas!\033[m')

    # ===================== 10 PERGUNTAS =====================
    elif perguntas == 10:

        resposta1 = input('Qual é o nome do navio que afundou em 1912 e virou um filme famoso?: ')
        if resposta1.strip().casefold() == 'titanic':
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta2 = input('Quem é conhecido como o "Rei do Pop"?: ')
        if resposta2.strip().casefold() == 'michael jackson':
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta3 = input('Quantas cores tem o arco-íris?: ')
        if resposta3.strip() == '7':
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta4 = input('Quem pintou a famosa obra "Monalisa"?: ')
        if resposta4.strip().casefold() == 'leonardo da vinci':
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta5 = input('Qual é o livro mais vendido no mundo (depois da Bíblia)?: ')
        if resposta5.strip().casefold() == 'dom quixote':
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta6 = input('Qual o nome do autor de "Sítio do Picapau Amarelo"?: ')
        if resposta6.strip().casefold() == 'monteiro lobato':
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta7 = input('Qual é o maior mamífero do mundo?: ')
        if resposta7.strip().casefold() == 'baleia azul':
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta8 = input('Quantos ossos tem o corpo humano adulto?: ')
        if resposta8.strip() == '206':
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta9 = input('Qual planeta é conhecido como o "Planeta Vermelho"?: ')
        if resposta9.strip().casefold() == 'marte':
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta10 = input('Qual o menor país do mundo?: ')
        if resposta10.strip().casefold() == 'vaticano':
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        print(f'\033[33mVocê acertou {len(acertos)} de 10 perguntas!\033[m')

    # ===================== 15 PERGUNTAS =====================
    elif perguntas == 15:

        resposta1 = input('Qual é o maior planeta do Sistema Solar?: ')
        if resposta1.strip().casefold() == 'jupiter':
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta2 = input('Qual é o nome da galáxia onde a Terra está localizada?: ')
        if resposta2.strip().casefold() in ['via lactea', 'via láctea']:
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta3 = input('Qual civilização construiu as pirâmides de Gizé?: ')
        if resposta3.strip().casefold() == 'egipcios':
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta4 = input('Quem foi o primeiro homem a orbitar a Terra?: ')
        if resposta4.strip().casefold() == 'yuri gagarin':
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta5 = input('Em que país ocorreu a Revolução Industrial?: ')
        if resposta5.strip().casefold() == 'inglaterra':
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta6 = input('Qual é a língua mais falada no mundo?: ')
        if resposta6.strip().casefold() == 'ingles':
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta7 = input('Em que ano o homem pisou na Lua pela primeira vez?: ')
        if resposta7.strip() == '1969':
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta8 = input('Qual o país mais populoso do mundo?: ')
        if resposta8.strip().casefold() in ['india', 'índia']:
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta9 = input('Quantos minutos tem uma hora?: ')
        if resposta9.strip() == '60':
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta10 = input('Qual é o rio mais longo do mundo?: ')
        if resposta10.strip().casefold() in ['nilo', 'rio nilo']:
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta11 = input('Quantos lados tem um hexágono?: ')
        if resposta11.strip() == '6':
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta12 = input('Qual é a cor da esmeralda?: ')
        if resposta12.strip().casefold() == 'verde':
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta13 = input('Qual é o nome do satélite natural da Terra?: ')
        if resposta13.strip().casefold() == 'lua':
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta14 = input('Qual gás nós respiramos para sobreviver?: ')
        if resposta14.strip().casefold() in ['oxigenio', 'oxigênio']:
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        resposta15 = input('Qual é a maior floresta tropical do mundo?: ')
        if resposta15.strip().casefold() in ['floresta amazonica', 'amazonia', 'amazônia']:
            print('\033[32mResposta correta!\033[m')
            acertos.append(1)
        else:
            print('\033[31mResposta incorreta!\033[m')

        print(f'\033[33mVocê acertou {len(acertos)} de 15 perguntas!\033[m')

    # ===================== CONTINUAR =====================
    continuar = input('Quer jogar de novo? (sim ou não): ')
    if continuar.strip().casefold() != 'sim':
        print('Valeu por jogar! 👋')
        break
