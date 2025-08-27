lista = ["Camisa", "Calca", "Blusa", "Jaqueta"]
print("IMPRESSAO 1: ", lista)

lista.append("Sapato")
print("IMPRESSAO 2: ", lista)

lista.insert(2, "Bone")
print("IMPRESSAO 3: ", lista)

if "Chapeu" in lista:
    lista.remove("Chapeu")
else:
    print("Nao ha chapeu na lista")

lista.sort()
print("IMPRESSAO FINAL: ", lista)