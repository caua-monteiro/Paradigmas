def fibo(x: int):
    a = 0
    b = 1
    c = 0

    if x == 1 or x == 2:
        return x-1 
    
    for i in range(x-2):
        c = a + b
        a = b
        b = c

    return c 

def main():
    x = int(input())
    print(fibo(x))
main()       