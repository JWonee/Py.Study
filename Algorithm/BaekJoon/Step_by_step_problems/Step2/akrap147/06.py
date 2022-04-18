# 백준 조건문 6번 문제
# 임의의 시간에서 임의의 시각을 더한 값은?

Hours , Minutes = map(int,input().split() )
Run_time = int(input())

Run_time_Hours = int(Run_time/60)
Run_time_Minutes = Run_time % 60

Minutes += Run_time_Minutes

if Minutes >= 60:
  Hours += 1 
  Minutes %= 60
Hours = Run_time_Hours + Hours 
if Hours >= 24:
  Hours %= 24

print(f"{Hours} {Minutes}")

# 05번에서도 사용했지만 fstring을 사용했다.
# fstring은 문자열과 변수를 동시에 출력이 가능하게 하는 방법이다.
# string처럼 사용하면서 중간중간 +없이 {변수}만 쓰면 바로 string안의 문자로 출력이 된다.
