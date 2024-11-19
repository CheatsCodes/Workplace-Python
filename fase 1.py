def obter_temperatura():
    while True:
        try:
            temperatura = float(input("Informe a temperatura máxima (em Celsius): "))
            if -60 <= temperatura <= 50:
                return temperatura
            else:
                print("Valor inválido. A temperatura deve estar entre -60°C e +50°C.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def obter_mes():
    while True:
        try:
            mes = int(input("Informe o número do mês (1 a 12): "))
            if 1 <= mes <= 12:
                return mes
            else:
                print("Valor inválido. Digite um número entre 1 e 12.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def main():
    total_meses = 12
    soma_temperaturas = 0
    meses_escaldantes = 0
    mes_mais_escaldante = None
    mes_menos_quente = None
    temperatura_maxima_anual = None

    for _ in range(total_meses):
        mes = obter_mes()
        temperatura = obter_temperatura()
        soma_temperaturas += temperatura

        if temperatura > 33:
            meses_escaldantes += 1

        if temperatura_maxima_anual is None or temperatura > temperatura_maxima_anual:
            temperatura_maxima_anual = temperatura
            mes_mais_escaldante = mes

        if mes_menos_quente is None or temperatura < temperatura_maxima_anual:
            mes_menos_quente = mes

    temperatura_media_anual = soma_temperaturas / total_meses

    # Mapeando números de mês para nomes de mês
    nomes_meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]

    print(f"Temperatura média máxima anual: {temperatura_media_anual:.2f}°C")
    print(f"Quantidade de meses escaldantes: {meses_escaldantes}")
    print(f"Mês mais escaldante do ano: {nomes_meses[mes_mais_escaldante - 1]}")
    print(f"Mês menos quente do ano: {nomes_meses[mes_menos_quente - 1]}")

if __name__ == "__main__":
    main()
