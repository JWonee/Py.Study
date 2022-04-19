print(' 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수,요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)')

A, B = map(int, input("A, B = ").split())
C = int(input("C = "))


A += (B+C)//60
B = (B+C)%60
  

if A == 24:
        A = 0

print(A, B) 




