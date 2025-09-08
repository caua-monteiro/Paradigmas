lista = ["Homer", "Marge", "Bart", "Lisa", "Maggie"]

for membro in lista:
    soma = 0
    for letra in membro:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            soma += 1
    print(membro, " tem ", soma, " vogais")