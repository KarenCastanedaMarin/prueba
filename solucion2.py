a=[
    [5,3,7],
    [7,9,0],
    [1,5,3]]

b=[
    [6,1,8], 
    [9,9,1], 
    [0,0,3]]

for i in range(0,3):
    for j in range(0,3):
        suma=0
        for w in range(0,3):
            suma+=a[i][j]*b[j][w]
        print(suma,end="\t")
    print()