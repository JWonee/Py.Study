# 14번 문제
n = num = int(input())
# input으로 n과 num을 할당 받는다. 
count = 0

while True:
    ten = n // 10   #//는 10을 나눴을 때 나오는 몫이다. 
    one = n % 10    #%는 나머지 연산자이다.
    total = ten + one
    count += 1
    
    n = int(str(n % 10) + str(total % 10))  #string으로 만들어서 이어 붙였다.
    if(num == n):
        break
print(count)
