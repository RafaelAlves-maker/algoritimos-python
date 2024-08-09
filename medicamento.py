
#Programa Principal

nome = ""
valor_barato = float("inf")
total_precos = 0

for i in range(5):
    medicamento = input(f"Digite o nome do medicamento {i + 1}: ")
    preco = float(input(f"Digite o preço do medicamento {i + 1} (em R$): "))

    # Atualiza o medicamento mais barato se o preço atual for menor
    if preco < valor_barato:
        nome = medicamento
        valor_barato = preco

    # Soma o preço ao total
    total_precos += preco

# Calcula a média dos preços
media_precos = total_precos / 5

# Exibe os resultados
print(f"\nO medicamento mais barato é {nome} e o preço é R$ {valor_barato:.2f}")
print(f"A média dos preços é R$ {media_precos:.2f}")


