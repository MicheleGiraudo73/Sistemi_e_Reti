import random
import string

def generatore_psw(n):
    
    psw_s = string.digits + string.ascii_letters #caratteri alfanumerici
    psw_c = string.digits + string.ascii_letters + string.punctuation #caratteri ascii

    if n == 1:
        k = 8
        tipo = psw_s
    else:
        k = 20
        tipo = psw_c

    psw = ""

    for x in range(k):
        char = random.choice(tipo)
        psw = psw + char
    
    print(psw)

i = int(input("inserire 1 per password semplice, 2 per password complicata "))
generatore_psw(i)