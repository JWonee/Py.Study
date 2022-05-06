N,X = map(int,input('N, X = ').split())

print(N,X)
A=[]

for i in range(N):
    k = int(input('input element of A : '))
    if k < X: 
        A.append(k)

print(A)
