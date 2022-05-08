n = int(input('n ='))

for i in range(n):
    ox_list = list(input('answer list ='))
    score = 0
    sum_score = 0

    for ox in ox_list:
        if ox == 'O':
            score += 1
            sum_score += score
        else:
            score = 0 #연속 O가 끝나면 문항 점수 값 초기화
    print(sum_score)
    break #왜 안 끝나는지 모르겠다
