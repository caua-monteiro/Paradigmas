def isTriangulo(a: float, b:float, c:float):
    if a < b+c and c < a+b and b < a+c:
        return True
    return False

def QuassificaTriangulo(a: float, b:float, c:float):
    if a == b and a == c:
        return "EQUILATERO"
    elif a != b and a != c and b != c:
        return "ESCALENO"
    else:
        return "ISOCELES"

def main():
    a = float(input())
    b = float(input())
    c = float(input())

    if isTriangulo(a, b, c):
        print(QuassificaTriangulo(a, b, c))
    else:
        print("Nao existe tringulo possivel")

main()