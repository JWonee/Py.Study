#2���� ������ ���� , input()���� sys�� stdin.readline()�� �� ������

import sys
 
inp = int(input())
for i in range(inp):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)
