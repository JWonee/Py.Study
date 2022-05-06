N = int(input('N='))
Nprime = N
count = 0
while True:
     a = Nprime //10
     b = Nprime % 10
     c = (a + b) %10
     Nprime = (b * 10) + c
     count += 1

     if (Nprime == N):
         break
print(count)





