def obter_dados():
    peso = float(input("Introduza o peso (kg): "))
    altura_cm = float(input("Introduza a altura (cm): "))
    return peso, altura_cm


def converter_altura(altura_cm):
    return altura_cm / 100


def calcular_imc(peso, altura_m):
    return peso / (altura_m * altura_m)


# imc = Índice de Massa Corporal
# tdp = Tipo de Peso

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Excesso de peso"
    else:
        return "Obesidade"

def main():
    peso, altura_cm = obter_dados()
    altura_m = converter_altura(altura_cm)

    imc = calcular_imc(peso, altura_m)
    imc = round(imc, 2)

    tdp = classificar_imc(imc)

    print("Classificação:", tdp)


main()