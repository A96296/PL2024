import sys

def ler_dataset(caminho_arquivo):
    linhas = []

    # Abre o arquivo em modo de leitura
    with open(caminho_arquivo, 'r') as arquivo:
        # Lê todas as linhas do arquivo
        linhas_arquivo = arquivo.readlines()

        # Ignora a primeira linha (cabeçalho)
        linhas_arquivo = linhas_arquivo[1:]

        # Processa cada linha
        for linha in linhas_arquivo:
            # Remove o caractere de quebra de linha no final
            linha = linha.strip()
            
            # Divide a linha pelos caracteres de vírgula para obter os valores
            valores = linha.split(',')

            # Adiciona os valores à lista de linhas
            linhas.append({
                'id': valores[0],
                'index': valores[1],
                'dataEMD': valores[2],
                'nome_primeiro': valores[3],
                'nome_ultimo': valores[4],
                'idade': valores[5],
                'genero': valores[6],
                'morada': valores[7],
                'modalidade': valores[8],
                'clube': valores[9],
                'email': valores[10],
                'federado': valores[11],
                'resultado': valores[12]
            })

    return linhas

def obter_modalidades_ordenadas(dataset):
    modalidades = set()

    for linha in dataset:
        modalidades.add(linha['modalidade'])

    modalidades_ordenadas = sorted(list(modalidades))
    
    return modalidades_ordenadas

def calcular_percentagens_aptidao(dataset):
    total_atletas = len(dataset)
    aptos_count = 0
    inaptos_count = 0

    for linha in dataset:
        resultado = linha['resultado'].lower()  # Converte para minúsculas para lidar com variações de capitalização
        if resultado == 'true':
            aptos_count += 1
        elif resultado == 'false':
            inaptos_count += 1

    # Calcula as percentagens
    percentagem_aptos = (aptos_count / total_atletas) * 100
    percentagem_inaptos = (inaptos_count / total_atletas) * 100

    return percentagem_aptos, percentagem_inaptos

def calcular_distribuicao_escalao_etario(dataset):
    distribuicao_escalao_etario = {}

    for linha in dataset:
        idade_str = linha['idade']

        # Tenta converter a string em um inteiro
        try:
            idade = int(idade_str)
        except ValueError:
            print(f"Aviso: A idade '{idade_str}' não é um número inteiro válido. Ignorando esta entrada.")
            continue

        # Calcula o escalão etário (intervalo de 5 anos)
        escalao = (idade // 5) * 5
        intervalo_escalao = f'[{escalao}-{escalao+4}]'

        # Adiciona ao dicionário de distribuição
        if intervalo_escalao in distribuicao_escalao_etario:
            distribuicao_escalao_etario[intervalo_escalao].append(linha)
        else:
            distribuicao_escalao_etario[intervalo_escalao] = [linha]

    return distribuicao_escalao_etario


# Exemplo de uso
caminho_do_arquivo = 'emd.csv'
dataset = ler_dataset(caminho_do_arquivo)
print(obter_modalidades_ordenadas(dataset))
print(calcular_percentagens_aptidao(dataset))
print(calcular_distribuicao_escalao_etario(dataset))

# Agora 'dataset' contém uma lista de listas, onde cada lista representa uma linha do arquivo CSV

