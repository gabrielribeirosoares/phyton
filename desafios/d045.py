from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0, 2)
print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
print('-=' *12)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-=' *12)
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador vence')
    elif jogador == 2:
        print''
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:

    elif jogador == 1:

    elif jogador == 2:
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:

    elif jogador == 1:

    elif jogador == 2:
    else:
        print('JOGADA INVÁLIDA')