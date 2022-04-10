#나
"""
print("첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수 A가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수 B가 주어진다.")

A,B = map(int, input("A,B = ").split())
B_str = str(B)

print( A*int(B_str[2]) , A*int(B_str[1]), A*int(B_str[0]), A*B , sep = '\n'  )
"""

#another sol

A = int(input( " A = "))
B_str = input("B = ")
B0 = int(B_str[0])
B1 = int(B_str[1])
B2 = int(B_str[2])
B = int(B_str)

print( A*B2 , A*B1, A*B0 , A*B , sep = '\n' )

# int , str 구분 주의!