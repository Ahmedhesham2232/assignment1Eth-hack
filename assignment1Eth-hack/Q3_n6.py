firstinrang = int(input("Enter the num1 in range : "))
lastinrang = int(input("Enter the num2 in range : "))

for n in range(firstinrang,lastinrang + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)
