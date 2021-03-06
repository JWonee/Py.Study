#내가 푼 코드
"""
A = int(input("Integer larger than 0 ; A = "))
B = int(input("Integer smaller than 10 ; B = "))

print(A + B)
"""

#another sol
"""
A,B = input().split() 
# input으로 A,B 를 입력 받고, split()함수로 나누어 A,B에 값 저장
#input()으로 어떤 문자던 입력 받음 >> split()은 괄호 안에 아무것도 없을 때, 공백을 기준으로 나눔
print(int(A)+int(B))
"""

# Q : 이거  왜 안되지? 
print("""
integer A is larger than 0
integer B is smaller than 10
""")
A,B = int(input()).split()
#윗줄 안됨. split() 쓰면 input을 int로 못 받아들이는 것인지..
print( A + B)

"""
= 왼쪽에 변수를 두고 = 오른쪽에 input( ) 함수를 작성하면 입력받은 문자를 변수에 선언할 수 있게 된다.

유의해야 할 점은 input 함수로 입력받는 것은 문자열로 입력받는다는 것이다. 사용자가 숫자를 입력하더라도 마찬가지로 문자열 형태로 입력받게 된다. 위의 예제 입력에서 보면  숫자 1과 2를 입력받는 게 아니라 '1 2'라는 숫자 두 개 사이에 공백이 있는 하나의 문자열을 입력받는 것이다.

변수를 A, B 두 개로 두고 split 함수를 사용한 것은 아래에서 마저 설명한다. 

다음으로 split( ) 함수는 입력받는 문자를 나눌 때 사용하는 함수이다. 위 문제에서 보면 숫자 두 개를 한 줄에 입력받는데 두 개의 숫자 사이에는 공백으로 구분되어 있다. 이런 경우에는 공백을 기준으로 숫자를 나누면 된다. 사용 형태는 문자열 뒤에 점을 붙이고 split( )을 써주면 된다. 위에서 input( ). split( )이라고 쓴 것은 입력받는 문자가 아직 정해지지 않았으나 어떤 문자이건 공백을 기준으로 나누겠다는 의미이다.

괄호 안에 아무것도 넣지 않으면 공백(띄어쓰기, 탭 등)을 기준으로 문자열을 나눈다. 

A, B = input( ). split( ) 문장에서 = 왼쪽에 A, B 두 개로 구분한 것은 튜플(tuple) 자료형의 성질을 이용한 것이다. = 우측에서 입력받은 문자를 공백을 기준으로 나누게 되면 두 개의 문자로 나누어지게 된다. 그 두 개의 문자를 각각 A, B 변수에 저장하겠다는 의미이다.
 input 함수로 입력을 받으면 문자열로 입력을 받게 된다고 했다. 그런데 이번 백준 문제에서 요구하는 것은 두 개의 수를 + 연산자로 더하는 것이다. 문자열에서도 + 연산자를 사용할 수 있으나 그건 수학처럼 숫자 두 개를 더하는 값을 출력하는 게 아니라 문자 두 개를 연달아 붙여버리는 기능이다. 그렇기 때문에 입력받은 두 개의 문자를 숫자로 변환하는 과정이 필요하다. 이때 int( ) 함수를 사용하면 숫자 형태의 두 개의 문자를 숫자로 변형할 수 있다. int는 숫자 중에서도 정수를 의미한다. 

이렇게 숫자로 변환해서 출력하면 두 수를 더한 값이 출력되게 된다
"""
