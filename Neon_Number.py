n=int(input())
s=0
sqr=n*n
while(sqr!=0):
    r=sqr%10
    s=s+r
    sqr=sqr//10
if(s==n):
    print('Neon Number')
else:
    print('Not Neon Number')