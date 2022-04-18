# 백준 조건문 5번 문제
# 45분 일찍 알람 설정하기

Hours , Minutes = map(int,input().split() )

if Hours != 0:
  if Minutes < 45:
    Hours -= 1
    Minutes = 60 - (45 - Minutes)
    print(f"{Hours} {Minutes}") 
  else:
    Minutes -= 45
    print(f"{Hours} {Minutes}")
else: 
  if Minutes < 45:
    Hours = 23
    Minutes = 60 - (45 - Minutes)
    print(f"{Hours} {Minutes}")
  else:
    Minutes -= 45
    print(f"{Hours} {Minutes}")
    
# another sol
H, M = map(int, input().split())

if M < 45 :	# 분단위가 45분보다 작을 때 
    if H == 0 :	# 0 시이면
        H = 23
        M += 60
    else :	# 0시가 아니면 (0시보다 크면)
        H -= 1	
        M += 60
        
print(H, M-45)	
# my sol의 문제점은 Hours가 0 에서 24로 넘어가는 기준으로 나눈게 착오다.
# Minutes이 45보다 큰지 작은지를 구분하는 개념이 앞에 말한 개념보다 더 큰 범위를 포괄하기에 처음 if문을 나눌때는 Minutes을 기준으로잡으면 훨씬 간결해진다.
