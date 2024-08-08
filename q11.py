a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
if a < b:
  soma = sum(range(a, b + 1))
  print(f"A soma dos números inteiros do intervalo [{a}, {b}] é {soma}")
else:
  print("ERRO")
