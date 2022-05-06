"""
N = int(input("N = "))


for i in range(1,N+1):
    print(i)
"""


[print(i) for i in range(1, int(input(' N = '))+1)] #Comprehension Case
    #[ 출력 표현식 for iterable자료 요소 in iterable자료형 ] 