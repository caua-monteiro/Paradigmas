def main():
    n = int(input())
    alunos = []
    for j in range(n):
        aux = {
            "nome": input(),
            "matricula": input(),
            "notas": float(input())
        }

        for aluno in alunos:
            if(aluno["matricula"] == aux["matricula"]):
                break
        else:
            alunos.append(aux)
    
    print(alunos)

main()