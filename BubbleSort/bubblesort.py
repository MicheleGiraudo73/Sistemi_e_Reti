def bubblesort(list):
    n=len(list)
    k=0
    j=0
    for k in range(n-1):
        for j in range(n-k-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j]=list[j+1]
                list[j+1]=temp
#--------------------------------------------------
lista = [10,9,8,6,5,4,31,2]

bubblesort(lista)
print(lista)

