import math

def funrec(i):
    a=math.trunc(((int(i) / 3) - 2))

    if a<0:
        return 0
    else:
        return  a + funrec(a)

f = open('file1', 'r')
suma=0;
for i in f:

    suma=suma+ funrec(i)

print(suma)






