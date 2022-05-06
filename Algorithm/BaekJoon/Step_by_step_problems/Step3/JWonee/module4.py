#2번과 동일한 문제 , input()보다 sys의 stdin.readline()이 더 빠르다

import sys
 
inp = int(input())
for i in range(inp):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)
