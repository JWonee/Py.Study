# 3번 문제
n = int(input())
hansu = 0
for i in range(n):
  if i+1 < 100:
    hansu += 1
  else:
    num = list(map(int,str(i+1)))
    if num[2] - num[1] == num[1] - num[0]:
      hansu += 1
print(hansu)
