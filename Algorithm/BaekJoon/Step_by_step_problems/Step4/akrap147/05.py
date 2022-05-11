# # 5번 문제
# 세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다. 일단 세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
# 예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.
# 세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.

Number_of_subject = int(input())
# 과목의 갯수
Scores = list(map(int, input().split()))
# 각각의 점수를 list의 element로 만들었다.
max = max(Scores)
# max(list)를 하면 list 속 element중 가장 큰 값이 반환된다.
Sum = 0
for i in range(Number_of_subject):
  Scores[i] = Scores[i]/max*100
  Sum += Scores[i]
average = Sum / Number_of_subject
print(average)

# max() 함수는 list에도 사용이 가능한게 특징이다. 
