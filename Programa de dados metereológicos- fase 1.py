# ============================================================
# PROJETO – FASE 1 - Programa de dados metereológicos1
# ============================================================

meses_extenso = {
    1: "janeiro", 
    2: "fevereiro", 
    3: "março", 
    4: "abril",
    5: "maio", 
    6: "junho", 
    7: "julho", 
    8: "agosto",
    9: "setembro", 
    10: "outubro", 
    11: "novembro", 
    12: "dezembro"
}

soma_temperaturas = 0
quantidade_escaldantes = 0
maior_temperatura = None
menor_temperatura = None
mes_mais_quente = None
mes_menos_quente = None

meses_lidos = 0

while meses_lidos < 12:

    # Validação do mês
    while True:
        try:
            mes = int(input("Informe o mês (1 a 12): "))
            if 1 <= mes <= 12:
                break
            else:
                print("Erro: o mês deve estar entre 1 e 12.")
        except ValueError:
            print("Erro: digite um número inteiro válido.")

    # Validação da temperatura
    while True:
        try:
            temperatura = float(input(f"Informe a temperatura máxima de {meses_extenso[mes]} (°C): "))
            if -60 <= temperatura <= 50:
                break
            else:
                print("Erro: temperatura deve estar entre -60°C e 50°C.")
        except ValueError:
            print("Erro: digite um número válido para a temperatura.")

    soma_temperaturas += temperatura

    if temperatura > 33:
        quantidade_escaldantes += 1

    if maior_temperatura is None or temperatura > maior_temperatura:
        maior_temperatura = temperatura
        mes_mais_quente = mes

    if menor_temperatura is None or temperatura < menor_temperatura:
        menor_temperatura = temperatura
        mes_menos_quente = mes

    meses_lidos += 1
    print("-" * 40)

media_anual = soma_temperaturas / 12

print("\n===== RESULTADOS =====")
print(f"Temperatura média máxima anual: {media_anual:.2f} °C")
print(f"Quantidade de meses escaldantes (>33°C): {quantidade_escaldantes}")
print(f"Mês mais escaldante do ano: {meses_extenso[mes_mais_quente]} ({maior_temperatura} °C)")
print(f"Mês menos quente do ano: {meses_extenso[mes_menos_quente]} ({menor_temperatura} °C)")