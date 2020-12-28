import random
import string

def mac():
    tipo = string.digits + "ABCDEF" #gli indirizzi MAC sono composti da cifre esadecimali quindi ho messo sia numeri che lettere fino alla F per l'esadecimale
    mac = ""
    #for che cicla per 6 volte, le 6 coppie degli indirizzi mac
    for x in range (6):
        #if che controlla di mettere solo 5 due punti 
        if x < 5:
            #for che forma ke coppie
            for k in range(2):
                coppia = random.choice(tipo)
                mac = mac + coppia
            mac = mac + ":"    
        else:
            for k in range(2):
                coppia = random.choice(tipo)
                mac = mac + coppia
                 
    print(mac)    

mac()