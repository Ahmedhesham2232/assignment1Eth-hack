
def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

# change this value for a different result
num =int(input("enter until the number do you need"))

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))

