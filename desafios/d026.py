frase = str(input('Digite uma frase: ')).upper().strip()
print('Na frase "{}", a letra A aparece {} vezes'.format(frase, frase.count('A')))
print('Aparece a primeira vez na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))