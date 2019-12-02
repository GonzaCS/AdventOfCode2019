import csv
import math
lista=[]
listacopia=[]

with open('file2', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        for i in row:
            lista.append(int(i))




for noun in range(99):
    for verb in range(99):
        i = 0
        listacopia=lista[:]
        listacopia[1]=noun
        listacopia[2]=verb
        while i< len(lista):
            if listacopia[i]==99:
                break
            a=listacopia[i+1]
            b=listacopia[i+2]
            c=listacopia[i+3]
            if listacopia[i]==1:
                listacopia[c]=listacopia[a]+listacopia[b]
            if listacopia[i]==2:
                listacopia[c]=listacopia[a]*listacopia[b]
            i+=4

        if listacopia[0]==19690720:
            break
    if(listacopia[0]==19690720):
        break



print( 100*noun + verb)

