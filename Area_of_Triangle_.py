import math
a,b,c=map(float,input().split())
s=((a+b+c)/2)
d=math.sqrt(s*(s-a)*(s-b)*(s-c))
print('{:.2f}'.format(d))