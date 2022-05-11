# 7번문제
# # 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
# 소숫점 셋째 자리 까지 출력해라 

n=int(input())
# 학생수 
for i in range(n):
    s=list(map(int,input().split()))
    avg=sum(s[1:])/s[0]
    count=0

    for i in s[1:]:
        if i>avg:
            count+=1

    print(f"{count/s[0]*100:.3f}%")
# 소숫점 3째자리 까지 쓸려면 :.3f라는 식을 써야한다. 
