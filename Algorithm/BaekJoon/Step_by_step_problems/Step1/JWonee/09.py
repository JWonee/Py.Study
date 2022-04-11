#나
"""
print("1 ≤ A, B ≤ 10,000 ; A,B are natural numbers")

A,B = map(int, input("A,B = ").split())

print(A + B) #덧셈
print(A - B) #뺄셈
print(A*B) #곱셈
print(int(A/B)) #나누기
#print(A//B)
print(A%B) #나머지
"""

#another sol

print("1 ≤ A, B ≤ 10,000 ; A,B are natural numbers")

A,B = map(int, input("A,B = ").split())

print( A+B, A-B, A*B, A//B, A%B, sep='\n')


#sep = '\n' 으로 줄바꾸기!
"""예제 출력 1의 출력 값을 보면 두 수를 계산한 각각의 값이 세로로 하나씩 출력되었다.
이런 규칙으로 출력될 하기 위해서 print 함수의 sep= 파라미터를 이용하였다. 
sep파라미터는 print 함수에서 쉼표로 구분된 각각의 출력 값 사이에 문자열을 삽입할 수 있다.
sep을 지정하지 않으면 기본값은 공백이어서 각각의 값이 가로로 공백 한 칸을 사이에 두고서 출력된다. 
이러한 성질을 이용해서 이스케이프 문자인 줄 바꿈 문자 '\n'를 출력 값 사이에 삽입하였다.
"""
