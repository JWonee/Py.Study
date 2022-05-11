# 6번 문제
# ox 퀴즈 점수 o가 반복이 되면 점수도 늘어난다.


n = int(input())
# 총 test횟수
for i in range(n):
    a = input()
    score = 0
    sum_Score = 0
    for j in a:
        if j == 'O':
            score += 1
#             여기서 'O'가 반복이 되면 점수가 쌓인다.
        else:
            score = 0
#       만약 X를 받았다면 score는 0으로 초기화가 되어 다시 0점부터 쌓아야한다. 
        sum_Score += score
#       각 시행의 결과를 즉시 score에 더한다.
    print(sum_Score)
