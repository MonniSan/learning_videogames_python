"""
Usar la formula general para resolver una ecuacion cuadratica. 
f(y) = a(x^2) + b(x) + c  f(y) tiende a 0
X = (-b +- srqrt((b*2 - (4a*c))))/2*a
"""

from math import sqrt

def solve(ca=1,cb=2,cc=1):
  discriminante = cb**2 - 4*ca*cc
  if discriminante < 0:
    x1= float ("-inf")
    x2= float ("inf")
    print (f"la ecuación no tiene solución real: {x1},{x2}")
    return x1, x2
  
  num1= -cb + sqrt(discriminante)
  num2= -cb - sqrt(discriminante)
  x1= num1/(2*ca)
  x2= num2/(2*ca)
  print (f"La solución es: {x1}, {x2}")
  return x1, x2

a=2
b=8
c=2

s11, s22 = solve()
print (f"solución = x1:{s11} x2:{s22}")

s111, s222 = solve (cc=5, cb=10)
print (f"solución = x1:{s111} x2:{s222}")

s2,s3 = solve (ca=1, cb=0, cc=2)

s1, s2 = solve(a,b,c) 
print (f"solución = x1:{s1} x2:{s2}")