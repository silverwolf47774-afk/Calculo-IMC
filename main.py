from collections import Counter


def ler_valor_positivo(mensagem, pode_ser_zero=False):
    while True:
        try:
            valor = float(input(mensagem))

            if valor < 0:
                print("Erro: o valor não pode ser negativo.")
            elif valor == 0 and not pode_ser_zero:
                print("Erro: o valor não pode ser zero.")
            else:
                return valor

        except ValueError:
            print("Erro: introduza um número válido.")


def obter_dados():
    peso = ler_valor_positivo("Introduza o peso (kg): ")
    altura_cm = ler_valor_positivo("Introduza a altura (cm): ")
    return peso, altura_cm


def converter_altura(altura_cm):
    return altura_cm / 100


def calcular_imc(peso, altura_m):
    return peso / (altura_m * altura_m)


# imc = Índice de Massa Corporal
# tdp = Tipo de Peso

def classificar_imc(imc):
    if imc < 18.5:
        return "Peso Baixo"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Excesso de peso"
    else:
        return "Obesidade"


def perguntar_continuar():
    while True:
        continuar = input("Deseja fazer outra consulta? (s/n): ").strip().lower()
        if continuar in ["s", "sim"]:
            return True
        elif continuar in ["n", "nao", "não"]:
            return False
        else:
            print("Erro: responda com 's' ou 'n'.")


def mostrar_resumo(total_consultas, lista_imc, contagem_classificacoes):
    media_imc = round(sum(lista_imc) / total_consultas, 2)
    tipo_mais_frequente = contagem_classificacoes.most_common(1)[0][0]

    print("\n=== RESUMO FINAL ===")
    print("Número total de consultas:", total_consultas)
    print("Média dos IMC calculados:", media_imc)
    print("Classificação mais frequente:", tipo_mais_frequente)


def main():
    total_consultas = 0
    lista_imc = []
    contagem_classificacoes = Counter()

    while True:
        peso, altura_cm = obter_dados()
        altura_m = converter_altura(altura_cm)

        if altura_m == 0:
            print("Erro: a altura não pode ser zero.")
            continue

        imc = calcular_imc(peso, altura_m)
        imc = round(imc, 2)
        tdp = classificar_imc(imc)

        print("Tipo de Peso:", tdp)

        total_consultas += 1
        lista_imc.append(imc)
        contagem_classificacoes[tdp] += 1

        if not perguntar_continuar():
            break

    if total_consultas > 0:
        mostrar_resumo(total_consultas, lista_imc, contagem_classificacoes)
    else:
        print("Não foram realizadas consultas.")


main()