import json


# Função para ler o arquivo dados.json
def carregar_dados_json(caminho='dados.json'):
    try:
        with open(caminho, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho}' não encontrado.")
        return None
    except json.JSONDecodeError:
        print("Erro: Falha ao decodificar o JSON.")
        return None


# Função principal contendo todas as etapas
def main():
    dados = carregar_dados_json()  # Carregar dados do JSON
    if not dados:
        return  # Se os dados não foram carregados, sair da função principal

    # **1) Cálculo do valor da variável SOMA**
    indice = 13
    soma = sum(range(1, indice + 1))  # Somar os números de 1 a 13
    print(f"Valor de SOMA após o processamento: {soma}")

    # **2) Verificar se um número pertence à sequência de Fibonacci**
    try:
        numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
    except ValueError:
        print("Erro: Por favor, insira um número válido.")
        return

    # Acessando a sequência de Fibonacci do JSON
    sequencia_fibonacci = dados.get("sequencia_fibonacci", [])
    if numero in sequencia_fibonacci:
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

    # **3) Cálculo do faturamento mensal**
    faturamento_dias = dados.get("faturamento_dias", [])
    if not faturamento_dias:
        print("Erro: Dados de faturamento não encontrados.")
        return

    faturamentos = [dia["faturamento"] for dia in faturamento_dias if dia["faturamento"] > 0]
    if faturamentos:
        menor_faturamento = min(faturamentos)
        maior_faturamento = max(faturamentos)
        media_faturamento = sum(faturamentos) / len(faturamentos)
        dias_acima_media = sum(1 for f in faturamentos if f > media_faturamento)

        print(f"Menor faturamento: R${menor_faturamento:.2f}")
        print(f"Maior faturamento: R${maior_faturamento:.2f}")
        print(f"Dias com faturamento acima da média: {dias_acima_media}")
    else:
        print("Não há faturamento válido para calcular.")

    # **4) Percentual de representação dos estados no faturamento**
    faturamento_estados = dados.get("faturamento_estados", {})
    if faturamento_estados:
        total_faturamento = sum(faturamento_estados.values())
        percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento_estados.items()}
        for estado, percentual in percentuais.items():
            print(f"{estado}: {percentual:.2f}%")
    else:
        print("Erro: Dados de faturamento por estado não encontrados.")

    # **5) Inverter os caracteres de uma string**
    string = input("Digite uma string para inverter: ")
    print(f"String invertida: {string[::-1]}")


# Executando a função principal
if __name__ == "__main__":
    main()
