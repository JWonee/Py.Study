print('(−1000 ≤ x ≤ 1000; x ≠ 0) , (−1000 ≤ y ≤ 1000; y ≠ 0)')
x,y = map(int,input("x,y = ").split())

if x > 0 :
    if y > 0:
        print(1)

    else:
        print(4)

else:
    if y > 0:
        print(2)

    else:
        print(3)