def obter_entrada_vendas():
    entrada = input(" ")

    entrada_list = entrada.split(',')
    vendas = list(map(int, entrada_list))

    return vendas


def analise_vendas(vendas):
    total_vendas = sum(vendas)
    media_vendas = total_vendas/ len(vendas)

    return f"{total_vendas}, {media_vendas}"





#chama as funções
vendas = obter_entrada_vendas()
print(analise_vendas(vendas))