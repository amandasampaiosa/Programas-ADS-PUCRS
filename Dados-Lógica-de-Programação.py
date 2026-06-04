
# =========================
def mes_mais_chuvoso(dados):
    chuva_por_mes = {}
    
    for d in dados:
        mes, ano = extrair_mes_ano(d["data"])
        chave = f"{mes}/{ano}"
        
        if chave not in chuva_por_mes:
            chuva_por_mes[chave] = 0
        
        chuva_por_mes[chave] += d["precip"]
    
    maior = max(chuva_por_mes, key=chuva_por_mes.get)
    
    print(f"Mês mais chuvoso: {maior}")
    print(f"Precipitação total: {chuva_por_mes[maior]:.2f}")


# =========================
# (C) MÉDIA TMIN
# =========================
def media_tmin_mes(dados, mes):
    medias = {}
    
    for ano in range(2006, 2017):
        soma = 0
        cont = 0
        
        for d in dados:
            m, a = extrair_mes_ano(d["data"])
            
            if m == mes and a == ano:
                soma += d["tmin"]
                cont += 1
        
        if cont > 0:
            medias[f"{mes}/{ano}"] = soma / cont
    
    return medias


# =========================
# (D) GRÁFICO
# =========================
def grafico(medias):
    anos = list(medias.keys())
    valores = list(medias.values())
    
    plt.bar(anos, valores)
    plt.xlabel("Ano")
    plt.ylabel("Temperatura mínima média")
    plt.title("Média da temperatura mínima")
    plt.xticks(rotation=45)
    
    plt.show()


# =========================
# (E) MÉDIA GERAL
# =========================
def media_geral(medias):
    soma = sum(medias.values())
    media = soma / len(medias)
    
    print(f"Média geral: {media:.2f}")


# =========================
# MENU PRINCIPAL
# =========================
def menu():
    dados = ler_dados("dados.csv")
    
    while True:
        print("\n1 - Visualizar dados")
        print("2 - Mês mais chuvoso")
        print("3 - Média temperatura mínima")
        print("4 - Gráfico")
        print("5 - Média geral")
        print("0 - Sair")
        
        op = int(input("Escolha: "))
        
        if op == 1:
            visualizar_dados(dados)
        
        elif op == 2:
            mes_mais_chuvoso(dados)
        
        elif op == 3:
            mes = int(input("Digite o mês: "))
            medias = media_tmin_mes(dados, mes)
            print(medias)
        
        elif op == 4:
            mes = int(input("Digite o mês: "))
            medias = media_tmin_mes(dados, mes)
            grafico(medias)
        
        elif op == 5:
            mes = int(input("Digite o mês: "))
            medias = media_tmin_mes(dados, mes)
            media_geral(medias)
        
        elif op == 0:
            break


menu()