import math

number1 = float(input("digite um número: "))
operator = input("digite uma operação: ")

if operator == "soma" or "sub" or "mult" or "div" or "expo":
    number2 = float(input("digite outro número: "))


def calculando():
    if operator == "soma":
        return number1 + number2
    elif operator == "sub":
        return number1 - number2
    elif operator == "mult":
        return number1 * number2
    elif operator == "div":
        return number1 / number2
    elif operator == "expo":
        return number1 / number2
    elif operator == "raiz":
        return math.sqrt(number1)
    elif operator == "porCem":
        return number1 / 100


print(calculando())
calculoFinal = calculando()

while True:
    operator2 = input("digite uma operação: ")

    if operator2 == "soma" or "sub" or "mult" or "div" or "expo":
        number3 = float(input("digite um número: "))

    def maisCalculo():
        if operator2 == "soma":
            return calculoFinal + number3
        elif operator2 == "sub":
            return calculoFinal - number3
        elif operator2 == "mult":
            return calculoFinal * number3
        elif operator2 == "div":
            return calculoFinal / number3
        elif operator == "expo":
            return number1 / number2
        elif operator == "raiz":
            return math.sqrt(calculoFinal)
        elif operator == "porCem":
            return calculoFinal / 100

    print(maisCalculo())
    calculoFinal = maisCalculo()
