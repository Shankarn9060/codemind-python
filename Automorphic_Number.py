n=int(input())
t=n
i=0
while(n>0):
 i+=1
 n=n//10
n=t*t
n=n%(pow(10,i))
if(t==n):
   print('Automorphic Number')
else:
   print('Not an Automorphic Number')