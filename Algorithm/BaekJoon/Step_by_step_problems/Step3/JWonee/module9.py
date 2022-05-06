'''
N = int(input('N = '))

stars = ''
for i in range(N):
    stars += '*'
    print(stars)
'''

inp = int(input())
for i in range(1,(inp+1)):
    print("*" * i)