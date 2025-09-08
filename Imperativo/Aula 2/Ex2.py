alunos = ["João", "Maria", "Pedro", "Ana"]
alunos.extend(["Carlos", "Beatriz"])

alunos.sort()

print(alunos)
removido = input()

if removido in alunos:
    alunos.remove(removido)
else:
    print("aluno nao existente")

for i in range(len(alunos)):
    if alunos[i] == "Ana":
        print(i)
        break
else:
    print("Ana nao esta na lista")

if(len(alunos) == 0):
    print("Lista vazia")
