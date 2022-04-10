print("A,B,C ; (2 ≤ A, B, C ≤ 10000)")
A,B,C = map(int, input("A,B,C = ").split())
print( (A+B)%C , ((A%C) + (B%C))%C , (A*B)%C , ((A%C)*(B%C))%C , sep = '\n')