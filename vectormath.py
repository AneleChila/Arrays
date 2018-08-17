# Vector maths
# Anele Chila
# 20 April 2016
import math
A = (input('Enter vector A:\n'))
A = A.split()
B = (input('Enter vector B:\n'))
B = B.split()
d = ''
c = 0
e = 0
f = 0
for i in range(len(A)):
    Sum = int(A[i])+int(B[i])
    Sum = str(Sum)
    d += Sum+','+' '
    Mult = int(A[i])*int(B[i])
    c += Mult
    e += int(A[i])**2
    f += int(B[i])**2
    
print('A+B =','['+d[:-2]+']')
print('A.B =',c)
print('|A| =','{0:<5.2f}'.format(math.sqrt(e),2))
print('|B| =','{0:<5.2f}'.format(math.sqrt(f),2))
    
    
    
   