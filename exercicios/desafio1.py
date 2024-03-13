valorHora = float(input("Quanto você ganha por hora? "))
horasTrabalhadas = float(input("Quantas horas você trabalha por mês? "))
salario = (valorHora*horasTrabalhadas)
print("Trabalhando {} horas por mês, sendo o valor da hora trabalhada = R${}, você irá receber R${}".format(horasTrabalhadas, valorHora, salario))