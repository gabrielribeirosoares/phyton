preco = float(input('Digite o valor do produto : R$'))
print('''FORMA DE PAGAMENTO
[ 1 ] à vista dinheiro
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual sua opção?'))
dinheiro = preco * 0.9
cartao = preco * 0.95
parcelado = preco / 2
parceladojuros = preco + (preco * 0.2)
if opcao == 1:
    print('O preço com desconto de 10% será de R${:.2f}'.format(dinheiro))
elif opcao == 2:
    print('O preço com desconto de 5% será de R${:.2f}'.format(cartao))
elif opcao == 3:
    print('Parcelado em 2x SEM JUROS, o valor da parcela será de R${:.2f} '.format(parcelado))
elif opcao == 4:
    totalparc = int(input('Quantas parcelas? '))
    parcela = parceladojuros / totalparc
    print('Parcelando em 3x ou mais COM JUROS de R${:.2f}, o valor total ficará R${:.2f}'.format(parcela, parceladojuros))