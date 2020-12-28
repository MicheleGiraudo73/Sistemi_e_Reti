def fibonacci(num):
    if num == 0:
        return 0 #la serie di fibonacci non è definità per i numeri negativi
    else:
        if num == 1:
            return 1
        else:
            return fibonacci(num - 1) + fibonacci(num - 2)

n = int(input("inserire il numero fino a che deve arrivare la serie, numero >= 0 "))

for k in range (n):
    print(fibonacci(k))