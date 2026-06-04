import os
import matplotlib.pyplot as plt

NOME_ARQUIVO = 'Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv'
ANO_INICIAL_MEDIA = 2006
ANO_FINAL_MEDIA = 2016


def localizar_arquivo_csv():
    """Retorna o nome do arquivo CSV na mesma pasta do programa.

    Primeiro tenta o nome esperado do projeto. Se não encontrar,
    procura qualquer arquivo .csv na pasta atual.
    """
    if os.path.exists(NOME_ARQUIVO):
        return NOME_ARQUIVO

    arquivos = os.listdir('.')
    for nome in arquivos:
        if nome.lower().endswith('.csv'):
            return nome
    return None



def converter_para_float(texto):
    """Converte texto para float.

    Tratamento adotado:
    - campo vazio -> None
    - vírgula decimal -> ponto
    - valor inválido -> None
    """
    texto = texto.strip().replace(',', '.')
    if texto == '':
        return None
    try:
        return float(texto)
    except ValueError:
        return None



def carregar_dados(nome_arquivo):
    """Lê o arquivo CSV e carrega os dados em uma lista de dicionários.

    Decisões de tratamento dos dados:
    - a primeira linha (cabeçalho) é ignorada;
    - linhas com quantidade de colunas diferente da esperada são descartadas;
    - linhas sem data válida são descartadas;
    - valores numéricos inválidos são armazenados como None;
    - o arquivo é acessado por caminho relativo, conforme o enunciado.
    """
    dados = []
    arquivo = open(nome_arquivo, 'r', encoding='utf-8-sig')

    cabecalho = arquivo.readline()
    if cabecalho == '':
        arquivo.close()
        return dados

    for linha in arquivo:
        linha = linha.strip()
        if linha == '':
            continue

        partes = linha.split(',')
        if len(partes) != 8:
            continue

        data = partes[0].strip()
        pedacos_data = data.split('/')
        if len(pedacos_data) != 3:
            continue

        if not (pedacos_data[0].isdigit() and pedacos_data[1].isdigit() and pedacos_data[2].isdigit()):
            continue

        dia = int(pedacos_data[0])
        mes = int(pedacos_data[1])
        ano = int(pedacos_data[2])

        if dia < 1 or dia > 31 or mes < 1 or mes > 12:
            continue

        registro = {
            'data': data,
            'dia': dia,
            'mes': mes,
            'ano': ano,
            'precipitacao': converter_para_float(partes[1]),
            'temperatura_maxima': converter_para_float(partes[2]),
            'temperatura_minima': converter_para_float(partes[3]),
            'umidade_relativa': converter_para_float(partes[6]),
            'velocidade_vento': converter_para_float(partes[7])
        }
        dados.append(registro)

    arquivo.close()
    return dados



def ler_inteiro(mensagem, minimo, maximo):
    while True:
        entrada = input(mensagem).strip()
        try:
            valor = int(entrada)
            if valor < minimo or valor > maximo:
                print('Valor inválido. Tente novamente.')
            else:
                return valor
        except ValueError:
            print('Entrada inválida. Digite um número inteiro.')



def ler_ano_valido(dados, mensagem):
    menor_ano = dados[0]['ano']
    maior_ano = dados[0]['ano']

    for registro in dados:
        if registro['ano'] < menor_ano:
            menor_ano = registro['ano']
        if registro['ano'] > maior_ano:
            maior_ano = registro['ano']

    return ler_inteiro(mensagem, menor_ano, maior_ano)



def formatar_valor(valor):
    if valor is None:
        return 'N/D'
    return f'{valor:.2f}'



def filtrar_periodo(dados, mes_inicial, ano_inicial, mes_final, ano_final):
    lista_filtrada = []

    for registro in dados:
        data_registro = (registro['ano'], registro['mes'])
        data_inicio = (ano_inicial, mes_inicial)
        data_fim = (ano_final, mes_final)

        if data_inicio <= data_registro <= data_fim:
            lista_filtrada.append(registro)

    return lista_filtrada



def exibir_cabecalho(tipo):
    if tipo == 1:
        print(f"{'Data':<12} {'Precip.':>10} {'Temp. Máx.':>12} {'Temp. Mín.':>12} {'Umidade':>10} {'Vento':>10}")
        print('-' * 70)
    elif tipo == 2:
        print(f"{'Data':<12} {'Precip.':>10}")
        print('-' * 24)
    elif tipo == 3:
        print(f"{'Data':<12} {'Temp. Máx.':>12} {'Temp. Mín.':>12}")
        print('-' * 38)
    else:
        print(f"{'Data':<12} {'Umidade':>10} {'Vento':>10}")
        print('-' * 34)



def visualizar_dados(dados):
    print('\nVISUALIZAÇÃO DE DADOS')
    mes_inicial = ler_inteiro('Informe o mês inicial (1 a 12): ', 1, 12)
    ano_inicial = ler_ano_valido(dados, 'Informe o ano inicial: ')
    mes_final = ler_inteiro('Informe o mês final (1 a 12): ', 1, 12)
    ano_final = ler_ano_valido(dados, 'Informe o ano final: ')

    if (ano_inicial, mes_inicial) > (ano_final, mes_final):
        print('Período inválido. A data inicial deve ser menor ou igual à final.')
        return

    print('\nEscolha o tipo de visualização:')
    print('1 - Todos os dados')
    print('2 - Apenas precipitação')
    print('3 - Apenas temperatura')
    print('4 - Apenas umidade e vento')
    tipo = ler_inteiro('Opção: ', 1, 4)

    dados_filtrados = filtrar_periodo(dados, mes_inicial, ano_inicial, mes_final, ano_final)

    if len(dados_filtrados) == 0:
        print('Não há dados para o período informado.')
        return

    print()
    exibir_cabecalho(tipo)

    for registro in dados_filtrados:
        if tipo == 1:
            print(
                f"{registro['data']:<12} "
                f"{formatar_valor(registro['precipitacao']):>10} "
                f"{formatar_valor(registro['temperatura_maxima']):>12} "
                f"{formatar_valor(registro['temperatura_minima']):>12} "
                f"{formatar_valor(registro['umidade_relativa']):>10} "
                f"{formatar_valor(registro['velocidade_vento']):>10}"
            )
        elif tipo == 2:
            print(f"{registro['data']:<12} {formatar_valor(registro['precipitacao']):>10}")
        elif tipo == 3:
            print(
                f"{registro['data']:<12} "
                f"{formatar_valor(registro['temperatura_maxima']):>12} "
                f"{formatar_valor(registro['temperatura_minima']):>12}"
            )
        else:
            print(
                f"{registro['data']:<12} "
                f"{formatar_valor(registro['umidade_relativa']):>10} "
                f"{formatar_valor(registro['velocidade_vento']):>10}"
            )

    print('\nTotal de registros exibidos:', len(dados_filtrados))



def calcular_mes_mais_chuvoso(dados):
    """Usa dicionário para somar a precipitação de cada mês/ano."""
    soma_precipitacao = {}

    for registro in dados:
        if registro['precipitacao'] is not None:
            chave = (registro['mes'], registro['ano'])
            if chave not in soma_precipitacao:
                soma_precipitacao[chave] = 0
            soma_precipitacao[chave] = soma_precipitacao[chave] + registro['precipitacao']

    maior_chave = None
    maior_valor = -1

    for chave in soma_precipitacao:
        if soma_precipitacao[chave] > maior_valor:
            maior_valor = soma_precipitacao[chave]
            maior_chave = chave

    return maior_chave, maior_valor



def mostrar_mes_mais_chuvoso(dados):
    chave, valor = calcular_mes_mais_chuvoso(dados)

    if chave is None:
        print('Não foi possível calcular o mês mais chuvoso.')
        return

    print('\nMÊS MAIS CHUVOSO')
    print('Mês/ano:', f'{chave[0]:02d}/{chave[1]}')
    print('Precipitação total:', f'{valor:.2f} mm')



def calcular_medias_minimas(dados, mes):
    """Usa dicionário para armazenar a média da temperatura mínima de 2006 a 2016."""
    temperaturas_por_ano = {}
    medias = {}

    for ano in range(ANO_INICIAL_MEDIA, ANO_FINAL_MEDIA + 1):
        temperaturas_por_ano[ano] = []

    for registro in dados:
        if registro['mes'] == mes and ANO_INICIAL_MEDIA <= registro['ano'] <= ANO_FINAL_MEDIA:
            if registro['temperatura_minima'] is not None:
                temperaturas_por_ano[registro['ano']].append(registro['temperatura_minima'])

    for ano in range(ANO_INICIAL_MEDIA, ANO_FINAL_MEDIA + 1):
        chave = str(mes).zfill(2) + '/' + str(ano)
        lista_temperaturas = temperaturas_por_ano[ano]

        if len(lista_temperaturas) > 0:
            soma = 0
            for valor in lista_temperaturas:
                soma = soma + valor
            medias[chave] = soma / len(lista_temperaturas)
        else:
            medias[chave] = None

    return medias



def mostrar_medias_minimas(dados):
    print('\nMÉDIA DA TEMPERATURA MÍNIMA (2006 a 2016)')
    mes = ler_inteiro('Informe o mês (1 a 12): ', 1, 12)
    medias = calcular_medias_minimas(dados, mes)

    for chave in medias:
        if medias[chave] is None:
            print(chave + ': N/D')
        else:
            print(chave + ': ' + f'{medias[chave]:.2f} °C')



def gerar_grafico_barras(dados):
    print('\nGRÁFICO DE BARRAS')
    mes = ler_inteiro('Informe o mês (1 a 12): ', 1, 12)
    medias = calcular_medias_minimas(dados, mes)

    anos = []
    valores = []

    for chave in medias:
        if medias[chave] is not None:
            anos.append(chave)
            valores.append(medias[chave])

    if len(valores) == 0:
        print('Não há dados suficientes para gerar o gráfico.')
        return

    plt.figure(figsize=(10, 5))
    plt.bar(anos, valores)
    plt.title('Médias da temperatura mínima do mês ' + str(mes).zfill(2) + ' (2006 a 2016)')
    plt.xlabel('Ano')
    plt.ylabel('Temperatura mínima média (°C)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



def mostrar_media_geral(dados):
    print('\nMÉDIA GERAL DA TEMPERATURA MÍNIMA')
    mes = ler_inteiro('Informe o mês (1 a 12): ', 1, 12)
    medias = calcular_medias_minimas(dados, mes)

    soma = 0
    quantidade = 0

    for chave in medias:
        if medias[chave] is not None:
            soma = soma + medias[chave]
            quantidade = quantidade + 1

    if quantidade == 0:
        print('Não há dados suficientes para calcular a média geral.')
    else:
        media_geral = soma / quantidade
        print('Média geral do mês', str(mes).zfill(2) + ':', f'{media_geral:.2f} °C')



def mostrar_menu():
    print('\n' + '=' * 56)
    print('PROJETO - DADOS CLIMÁTICOS DE PORTO ALEGRE')
    print('=' * 56)
    print('1 - Visualizar intervalo de dados')
    print('2 - Mês mais chuvoso')
    print('3 - Média da temperatura mínima de um mês')
    print('4 - Gráfico de barras das médias da temperatura mínima')
    print('5 - Média geral da temperatura mínima de um mês')
    print('0 - Sair')



def main():
    nome_arquivo = localizar_arquivo_csv()

    if nome_arquivo is None:
        print('Nenhum arquivo CSV foi encontrado na mesma pasta do programa.')
        return

    dados = carregar_dados(nome_arquivo)

    if len(dados) == 0:
        print('Nenhum dado válido foi carregado do arquivo.')
        return

    print('Arquivo carregado com sucesso:', nome_arquivo)
    print('Quantidade de registros válidos:', len(dados))

    opcao = -1
    while opcao != 0:
        mostrar_menu()
        opcao = ler_inteiro('Escolha uma opção: ', 0, 5)

        if opcao == 1:
            visualizar_dados(dados)
        elif opcao == 2:
            mostrar_mes_mais_chuvoso(dados)
        elif opcao == 3:
            mostrar_medias_minimas(dados)
        elif opcao == 4:
            gerar_grafico_barras(dados)
        elif opcao == 5:
            mostrar_media_geral(dados)
        elif opcao == 0:
            print('Programa encerrado.')


if __name__ == '__main__':
    main()
