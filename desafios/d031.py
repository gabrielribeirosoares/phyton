distancia = float(input('Qual é a distância da viagem? '))
print('Você está prestes a começar uma viagem de {:.0f} km'.format(distancia))
if distancia > 200:
    preço = distancia * 0.45
else:
    preço = distancia * 0.50
print('E o preço da sua passagem será de R${:.2f}'.format(preço))

