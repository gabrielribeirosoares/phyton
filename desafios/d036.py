print('Bem-vindo(a) ao Centro de Empréstimos da Rede Federal')
valorcasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
tempo = int(input('Em quantos anos você vai pagar? '))
prestacao = (valorcasa / (tempo*12))
parcela = (salario * 0.30)
if prestacao >= parcela:
    print('Infelizmente seu pedido foi negado pois seu salário ficará mais de 30% comprometido')
else:
    print('Parabéns, seu empréstimo foi aprovado!')
    print('Com seu salário de R${:.2f}, você consegue adquirir uma casa no valor de R${:.2f}'.format(salario, valorcasa))
    print('Pagando prestações de R${:.2f} em {} anos'.format(prestacao, tempo))
