from datetime import date
atual = (date.today().year)
nascimento = int(input('Digite o ano do seu nascimento: '))
idade = atual - nascimento
if idade <= 9:
    print('Para quem nasceu em {}, tem {} anos em {}'.format(nascimento, idade, atual))
    print('Você faz parte da categoria MIRIM')
elif idade <= 14:
    print('Para quem nasceu em {}, tem {} anos em {}'.format(nascimento, idade, atual))
    print('Você faz parte da categoria INFANTIL')
elif idade <= 19:
    print('Para quem nasceu em {}, tem {} anos em {}'.format(nascimento, idade, atual))
    print('Você faz parte da categoria JUNIOR')
elif idade == 25:
    print('Para quem nasceu em {}, tem {} anos em {}'.format(nascimento, idade, atual))
    print('Você faz parte da categoria SÊNIOR')
elif idade > 25:
    print('Para quem nasceu em {}, tem {} anos em {}'.format(nascimento, idade, atual))
    print('Você faz parte da categoria MASTER')

