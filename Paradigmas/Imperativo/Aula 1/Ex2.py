def setOrdem(a: float, b:float, c:float):
    if a > b and a > c:
        if b > c:
            return a, b, c
        else:
            return a, c, b
    elif b > a and b > c:
        if a > c:
            return b, a, c
        else:
            return b, c, a
    else:
        if a > b:
            return c, a, b
        else:
            return c, b, a
        
def main():
    a = float(input())
    b = float(input())
    c = float(input())

    a, b, c = setOrdem(a, b, c)
    print(c, b, a)

main()