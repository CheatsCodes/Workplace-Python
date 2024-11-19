def obter_mes():
    while True:
        try:
            mes = int(input("Informe um mês do ano (1-12): "))
            if 1 <= mes <= 12:
                return mes
            else:
                print("Erro: O mês deve estar entre 1 e 12.")
        except ValueError:
            print("Erro: Por favor, insira um número válido.")

def obter_temperatura():
    while True:
        try:
            temp = float(input("Informe a temperatura máxima do mês (em Celsius): "))
            if -60 <= temp <= 50:
                return temp
            else:
                print("Erro: A temperatura deve estar entre -60 e 50 graus Celsius.")
        except ValueError:
            print("Erro: Por favor, insira um número válido.")

def main():
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    temperaturas = []

    for i in range(12):
        print(f"\nMês: {meses[i]}")
        temp = obter_temperatura()
        temperaturas.append(temp)

    temp_media_max = sum(temperaturas) / len(temperaturas)
    meses_escaldantes = sum(1 for temp in temperaturas if temp > 33)
    mes_mais_escaldante = meses[temperaturas.index(max(temperaturas))]
    mes_menos_quente = meses[temperaturas.index(min(temperaturas))]

    print(f"\nTemperatura média máxima anual: {temp_media_max:.2f}°C")
    print(f"Quantidade de meses escaldantes: {meses_escaldantes}")
    print(f"Mês mais escaldante do ano: {mes_mais_escaldante}")
    print(f"Mês menos quente do ano: {mes_menos_quente}")

if __name__ == "__main__":
    main()
