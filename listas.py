pe = []
while True:
    nome = input("Nome do eletrônico: ")
    pe.append(nome)
    resp = input("Deseja adicionar outro? (s|n): ").upper()
    if resp == "N":
        break

print(pe)
