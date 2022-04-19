#나
"""
print("-10,000 ≤ A, B ≤ 10,000")
A,B = map(int,input("A = , B = ").split())

if A > B:
    print(" > " )

elif A < B:
    print(" < ")

else :
    print("==")

"""

#삼항 연산자 코드
#조건식 1이 참일 때 값 if 조건식 1 else [ 조건식2가 참일 때 값 if 조건식2 else 조건식이 모두 거짓일 때 값 ]

print("-10,000 ≤ A, B ≤ 10,000")
A,B = map(int,input("A = , B = ").split())

print('>') if A > B else print('<') if A < B else print('==')
