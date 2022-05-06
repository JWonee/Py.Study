t = int(input("# of test cases :"))

for i in range(1,t+1):
    A,B = map(int,input("A,B=").split())
    print("Case #",i,":",A," + ",B, " = ",A+B)
