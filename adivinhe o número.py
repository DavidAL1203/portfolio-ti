from time import sleep
from random import randint
def jogar():
    vd = vidas1 = jogador = 0
    tutorial1 = ' '
    print('\033[35m='*53)
    print(f'{'\033[34mADIVINHE O NÚMERO':^58}')
    print('\033[35m='*53)
    while True:
        modo = int(input(f'{'\033[35mMODO DE JOGO':30}\n'
                         '\033[33m[ 1 ]\033[36m p1 vs PC\n'
                         '\033[33m[ 2 ]\033[36m p1 vs p2\n'
                         '\033[33m[ 3 ]\033[31m Sair do jogo\n'
                         '\033[34mEM QUAL MODO QUER JOGAR: \033[m'))
        print('\033[35m=' * 53)
        if modo == 1:
            while True:
                sairjogo1 = False
                if tutorial1 == ' ':
                    tutorial1 = str(input('\033[34mVer tutorial? \033[36m[SIM] / [NÃO] ')).strip().upper()[0]
                if tutorial1 in 'SN':
                    if tutorial1 == 'S':
                        print(f'\033[35m{' COMO JOGAR ':=^{53}}')
                        sleep(1)
                        print('\033[33m-> O objetivo do jogo é adivinhar um número de 1 a 500.')
                        sleep(0.5)
                        print('-> O jogador tera um número de vidas conforme a dificuldade escolhida.')
                        sleep(0.5)
                        print('-> Se o jogador acertar o número, as vidas do jogador são resetadas e uma nova rodada é iniciada.')
                        sleep(0.5)
                        print('-> A cada tentativa de adivinhar o número o jogador perde uma vida.')
                        sleep(0.5)
                        print('-> O jogador vence a rodada quando adivinhar o numero, marcando um ponto.')
                        sleep(0.5)
                        print('-> Se o jogador perder uma rodada o jogo acaba e o jogador perde.')
                        sleep(0.5)
                        print('-> O jogador vence o jogo quando marcar 10 pontos.')
                        sleep(1)
                        print('\033[35m='*53)
                        sleep(2)
                        tutorial1 = 'pass'
                    if tutorial1 == 'N':
                        print('\033[35m=' * 53)
                        sleep(0.5)
                        tutorial1 = 'pass'
                elif tutorial1 != 'pass' and tutorial1 != 'N' and tutorial1 != 'S':
                    print('\033[31mOpção invalida!')
                    tutorial1 = ' '
                while tutorial1 == 'pass':
                    dificuldade1 = str(input('\033[35mDIFICULDADE DO JOGO:\n'
                                             f'\033[33m[{'Iniciante':^11}]\033[36m 15 vidas\n'
                                             f'\033[33m[{'Fácil':^11}]\033[36m 12 vidas\n'
                                             f'\033[33m[{'Médio':^11}]\033[36m 10 vidas\n'
                                             f'\033[33m[{'Difícil':^11}]\033[36m 7 vidas\n'
                                             f'\033[33m[{'PRÓ':^11}]\033[36m 5 vidas\n'
                                             f'\033[33m[{'LENDÁRIO':^11}]\033[36m 2 vidas\n'
                                             '\033[34m Em qual dificuldade quer jogar? ')).upper().strip()[0]
                    dificuldade = ' '
                    if dificuldade1 == 'I':
                        dificuldade = 'Iniciante'
                        vidas1 = 15
                        vd = 15
                    elif dificuldade1 == 'F':
                        dificuldade = 'Facil'
                        vidas1 = 12
                        vd = 12
                    elif dificuldade1 == 'M':
                        dificuldade = 'Médio'
                        vidas1 = 10
                        vd = 10
                    elif dificuldade1 == 'D':
                        dificuldade = 'Difícil'
                        vidas1 = 7
                        vd = 7
                    elif dificuldade1 == 'P':
                        dificuldade = 'PRÓ'
                        vidas1 = 5
                        vd = 5
                    elif dificuldade1 == 'L':
                        dificuldade = 'LENDÁRIO'
                        vidas1 = 2
                        vd = 2
                    else:
                        print('\033[31m Opção invalida!')
                    if dificuldade1 in 'IFMDPL':
                        pc = randint(1, 500)
                        print('\033[35m=' * 53)
                        print(f'\033[35mVocê escolheu a dificuldade {dificuldade}.\n'
                              f'Você tem {vd} vidas, adivinhe o número de 1 a 500...')
                        while True:
                            rodada = 1
                            pontos = 0
                            if pontos == 10:
                                break
                            while rodada < 11:
                                print('\033[35m=' * 53)
                                print(f'Rodada {rodada}!!!')
                                print(f'\033[31mVidas: {vidas1}')
                                print(f'\033[32mPontos: {pontos}')
                                if vidas1 > 0:
                                    jogador = int(input('\033[34mQual é o seu palpite? '))
                                    if jogador == pc:
                                        print(f'\033[36mVocê venceu a {rodada}º rodada!')
                                        pontos += 1
                                        vidas1 = vd
                                        rodada += 1
                                    elif jogador > pc:
                                        print('\033[33mO número é menor que seu palpíte...')
                                        vidas1 -= 1
                                    elif jogador < pc:
                                        print('\033[33mO número é maior que seu palpite...')
                                        vidas1 -= 1
                                if vidas1 == 0:
                                    print(f'\033[33mO número era {pc}!')
                                    print('\033[31mGAME OVER!')
                                    print('\033[35mReiniciando...')
                                    sairjogo1 = True
                                    tutorial1 = ' '
                                    sleep(2)
                                    print('\033[35m=' * 53)
                                    break
                                if pontos == 10:
                                    print('\033[32mVOCÊ VENCEU! FIM DE JOGO!')
                                    print('\033[35mReiniciando...')
                                    sairjogo1 = True
                                    tutorial1 = ' '
                                    sleep(2)
                                    print('\033[35m=' * 53)
                                    break
                                if pc == jogador:
                                    pc = randint(1, 500)
                            if sairjogo1:
                                break
                    if sairjogo1:
                        break
                if sairjogo1:
                    break
        elif modo == 2:
            while True:
                sairmodo2 = False
                if tutorial1 == ' ':
                    tutorial1 = str(input('\033[34mVer tutorial? \033[36m[SIM] / [NÃO] ')).strip().upper()[0]
                if tutorial1 in 'SN':
                    if tutorial1 == 'S':
                        print(f'\033[35m{' COMO JOGAR ':=^{53}}')
                        sleep(1)
                        print('\033[33mO objetivo do jogo é adivinhar um número de 1 a 500.')
                        sleep(0.5)
                        print('Os jogadores tem 5 chances em cada rodada para adivinhar o número.')
                        sleep(0.5)
                        print('Se o jogador acertar o número, ele recebe um ponto e vence a rodada.')
                        sleep(0.5)
                        print('Se nenhum jogador acertar o número, o ponto vai para quem chegar mais perto de acertar.')
                        sleep(0.5)
                        print('O jogador que fazer 5 pontos primeiro vence.')
                        sleep(0.5)
                        print('Se o jogo empatar, uma nova rodada se inicia para desempate.')
                        sleep(0.5)
                        print('O jogador vence o jogo quando marcar 10 pontos.')
                        sleep(2)
                        print('\033[35m=' * 53)
                        sleep(1)
                        tutorial1 = 'pass'
                    if tutorial1 == 'N':
                        print('\033[35m=' * 53)
                        sleep(0.5)
                        tutorial1 = 'pass'
                elif tutorial1 != 'pass' and tutorial1 != 'N' and tutorial1 != 'S':
                    print('\033[31mOpção invalida!')
                    tutorial1 = ' '
                while tutorial1 == 'pass':
                    while True:
                        rodada = 1
                        pontos1 = pontos2 = 0
                        chances = 5
                        fimdejogo = False
                        pc = randint(1, 500)
                        player1 = str(input('\033[34mNome do player 1: ')).upper().strip()
                        player2 = str(input('\033[34mNome do player 2: ')).upper().strip()
                        print(f'\033[35m{' INICIANDO JOGO ':=^{53}}')
                        while not fimdejogo:
                            print(f'\033[34mRODADA {rodada}!!!')
                            print(f'\033[31mPalpites restantes: {chances}')
                            print(f'\033[32m{player1}: {pontos1}\n'
                                  f'\033[32m{player2}: {pontos2}')
                            j1 = int(input(f'\033[35mVez de {player1}\n'
                                           f'\033[34mQual o seu palpite? '))
                            j2 = int(input(f'\033[35mVez de {player2}\n'
                                           f'\033[34mQual o seu palpite? '))
                            if j1 == pc and j2 != pc:
                                print(f'\033[36m{player1} Venceu a rodada {rodada} e marcou 1 ponto!')
                                print(f'\033[35mO número era {pc}')
                                chances = 5
                                rodada += 1
                                pontos1 += 1
                                pc = randint(1, 500)
                            elif j2 == pc and j1 != pc:
                                print(f'\033[36m{player2} Venceu a rodada {rodada} e marcou 1 ponto!')
                                print(f'\033[35mO número era {pc}')
                                chances = 5
                                rodada += 1
                                pontos2 += 1
                                pc = randint(1, 500)
                            elif j1 == j2 and j1 != pc:
                                if j1 > pc:
                                    print('\033[33mO número é menor que o palpite dos jogadores')
                                    chances -= 1
                                elif j1 < pc:
                                    print('\033[33mO número é maior que o palpite dos jogadores')
                                    chances -= 1
                            elif j1 == j2 == pc:
                                print('\033[36mEmpate! Os dois jogadores marcaram 1 ponto!')
                                print(f'\033[35mO número era {pc}')
                                rodada += 1
                                chances = 5
                                pontos1 += 1
                                pontos2 += 1
                                pc = randint(1, 500)
                            elif j1 != j2 != pc:
                                if j1 > pc and j2 > pc:
                                    print('\033[33mO número é menor que o palpite dos jogadores')
                                elif j1 < pc and j2 < pc:
                                    print('\033[33mO número é maior que o palpite dos jogadores')
                                elif j1 > pc:
                                    print(f'\033[33mO número é menor que o palpite de {player1} ', end='')
                                    if j2 > pc:
                                        print(f'e menor que o palpite de {player2}')
                                    elif j2 < pc:
                                        print(f'e maior que o palpite de {player2}')
                                elif j1 < pc:
                                    print(f'\033[33mO número é maior que o palpite de {player1} ', end='')
                                    if j2 > pc:
                                        print(f'e menor que o palpite de {player2}')
                                    elif j2 < pc:
                                        print(f'e maior que o palpite de {player2}')
                                chances -= 1
                            if chances == 0:
                                if j1 > pc:
                                    soma1 = j1 - pc
                                else:
                                    soma1 = pc - j1
                                if j2 > pc:
                                    soma2 = j2 - pc
                                else:
                                    soma2 = pc - j2
                                if soma1 < soma2:
                                    print(f'\033[36m{player1} Venceu a rodada {rodada} e marcou 1 ponto!')
                                    print(f'\033[35mO número era {pc}')
                                    rodada += 1
                                    chances = 5
                                    pontos1 += 1
                                elif soma1 > soma2:
                                    print(f'\033[36m{player2} Venceu a rodada {rodada} e marcou 1 ponto!')
                                    print(f'\033[35mO número era {pc}')
                                    rodada += 1
                                    chances = 5
                                    pontos2 += 1
                                elif soma1 == soma2:
                                    print('\033[36mEmpate! Os dois jogadores marcaram 1 ponto!')
                                    print(f'\033[35mO número era {pc}')
                                    rodada += 1
                                    chances = 5
                                    pontos1 += 1
                                    pontos2 += 1
                                pc = randint(1, 500)
                            print('\033[35m=' * 53)
                            if pontos1 > 4 or pontos2 > 4:
                                denovo = ' '
                                if pontos1 > pontos2:
                                    print('\033[32mO grande vencedor é... ', end='')
                                    sleep(2)
                                    print(f'\033[34m{player1}!!!')
                                    while denovo not in 'SN':
                                        denovo = str(input('\033[34mQuer jogar novamente? [S/N] ')).upper().strip()[0]
                                        if denovo == 'S':
                                            print('\033[35mReiniciando...')
                                            fimdejogo = True
                                        elif denovo == 'N':
                                            print('\033[31mSaindo...')
                                            tutorial1 = ' '
                                            sleep(1)
                                            print('\033[35m=' * 53)
                                            fimdejogo = True
                                            sairmodo2 = True
                                            break
                                        else:
                                            print('\033[31mOpção invalida!')
                                elif pontos2 > pontos1:
                                    print('\033[32mO grande vencedor é... ', end='')
                                    sleep(2)
                                    print(f'\033[34m{player2}!!!')
                                    while denovo not in 'SN':
                                        denovo = str(input('\033[34mQuer jogar novamente? [S/N] ')).upper().strip()[0]
                                        if denovo == 'S':
                                            print('\033[35mReiniciando...')
                                            fimdejogo = True
                                        elif denovo == 'N':
                                            print('\033[31mSaindo...')
                                            tutorial1 = ' '
                                            sleep(1)
                                            print('\033[35m=' * 53)
                                            fimdejogo = True
                                            sairmodo2 = True
                                            break
                                        else:
                                            print('\033[31mOpção invalida!')
                                elif pontos1 == pontos2:
                                    print('\033[31mEMPATE CRITICO! Rodada de desempate...')
                            if sairmodo2:
                                break
                        if sairmodo2:
                            break
                    if sairmodo2:
                        break
                if sairmodo2:
                    break
        elif modo == 3:
            break
        else:
            print('\033[31mOpção invalida!')
jogar()
while True:
    sair = str(input('\033[31mATENÇÃO! VOCÊ ESTÁ SAINDO DO JOGO. DESEJA SAIR? [S/N] ')).upper().strip()[0]
    sleep(0.5)
    if sair == 'S':
        break
    elif sair == 'N':
        print('\033[35mReiniciando...')
        sleep(1)
        jogar()
    else:
        print('\033[31mOpção invalida!')
print('\033[35mVolte sempre!')
print('\033[31mSaindo...')
sleep(2)
