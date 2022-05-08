A,B,C = map(int,input('A,B,C=').split())

product = list(str(A*B*C)) 

for i in range(10):
    print(product.count(str(i)))

