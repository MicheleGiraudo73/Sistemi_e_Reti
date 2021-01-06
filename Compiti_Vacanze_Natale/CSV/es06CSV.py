def diz():
    file = open("annual.csv","r")

    anomalie = {}
    k=0
    a=0 
    for riga in file:
        linea = riga.split(',')

        if linea[1] == "Year":
            continue
        else:
            a += float(linea[2])
            k += 1
            if(k==2):
                anomalie[int(linea[1])] = a / k
                k=0
                a=0

    return anomalie

def maxMin(anomalie,anno1, anno2):
    min = anomalie[anno1]
    max = anomalie[anno1]

    if anno1 > anno2:
        anno2,anno1 = anno1,anno2

    for v in range(anno1,anno2):
        if anomalie[v] > max:
            max = anomalie[v]
        else:
            if anomalie[v] < min:
                min = anomalie[v]
    print(min,max)

l = diz()

anno1 = int(input("inserire primo anno"))
anno2 = int(input("inserire secondo anno"))
maxMin(l,anno1,anno2)



