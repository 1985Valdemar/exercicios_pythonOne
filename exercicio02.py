from collections import Counter

def produto_mais_vendido(produtos):
    # Usar Counter para contar a ocorrência de cada produto
    contagem = Counter(produtos)
    
    # Encontrar o produto com a maior contagem
    max_produto = max(contagem, key=contagem.get)
    
    return max_produto


def obter_entrada_produtos():
    while True:
        entrada = input('Insira produtos (separados por vírgula): ')
        if entrada.strip():
            # Retornar lista de produtos já limpa de espaços em branco
            return [produto.strip() for produto in entrada.split(',')]
        else:
            print('Entrada inválida. Por favor, tente novamente.')


def main():
    try:
        produtos = obter_entrada_produtos()
        produto_mais_vendido_result = produto_mais_vendido(produtos)
        print(f'O produto mais vendido é: {produto_mais_vendido_result}')
    except Exception as e:
        print(f'Erro: {e}')

# Executar a função principal
if __name__ == "__main__":
    main()
# maçã, banana, maçã, laranja, banana, maçã
