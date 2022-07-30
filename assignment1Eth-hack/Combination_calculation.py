def factorialn(n):
   if n == 1:
       return n
   else:
       return n*factorialn(n-1)

def combination(n,r):
    fn=factorialn(n)
    fr=factorialn(r)
    fnr=factorialn(n-r)
   
    return fn/(fr*fnr)


n=int(input("enter the first number"))
r=int(input("enter the second number"))

print(combination(n,r))