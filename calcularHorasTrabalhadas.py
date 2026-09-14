horasTrabalhadas = input("digite suas horas trabalhadas: (hh:mm:ss)\n")
salarioHora = float(input("digite qual o seu salário a hora: (R$ 00.00)\n"))

horasSplit = horasTrabalhadas.split(":")

horas = float(horasSplit[0])
minutos = float(horasSplit[1])
segundos = float(horasSplit[2])

horasTotais = horas + (minutos / 60) + (segundos / 3600)

calcFinal = horasTotais * salarioHora

print(f"o seu salário é: R${calcFinal:.2f}")
