from math import sqrt

def solve(pa=1,pb=2,pc=1):
  x1 = -pb + sqrt(pb**2 - 4*pa*pc)
  x2 = -pb - sqrt(pb**2 - 4*pa*pc)
  return x1/(2*pa), x2/(2*pa)

a=2
b=8
c=2

s11, s22 = solve()
print (f"solución = x1:{s11} x2:{s22}")

s111, s222 = solve (pc=5, pb=10)
print (f"solución = x1:{s111} x2:{s222}")

s1, s2 = solve(a,b,c) 
print (f"solución = x1:{s1} x2:{s2}")