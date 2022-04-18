# 백준 조건문 4번 문제
# 좌표값이 몇사분면에 위치해 있는지 출력하기
x = int(input())
y = int(input())

if x > 0 :
  if y > 0:
    print("1")
  elif y < 0:
    print("4")
elif x < 0 :
  if y >0:
    print("2")
  elif y< 0:
    print("3")
    
    
