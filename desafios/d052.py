n1 = int(input('Digite um número: '))
tot = 0
for c in range (1, n1 + 1):
    if n1 % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\33[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[m O número {} foi divisível {} vezes'.format(n1, tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')

