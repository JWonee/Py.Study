a,b,c = map(int, input('a,b,c = ').split())

if a == b == c:
    print(10000 + a*1000)
elif a == b or a == c:
    print(1000 + a*100)
elif b == c:
    print(1000 + b*100)

else:
    print(max(a,b,c)*100)





"""
if a == b:

    if b == c:
    else:

elif a == c:

elif b == c:

else:
    if a>b:
        if a>c:
        else:
    else:
        if b > c:
        else:

"""

