#palindrome 

def ispalindrome(w):

  rev = ''.join(reversed(w))

  
  if(w == rev):
     return True
  return False

# main function
word=input("Enter the word ")
ckeck = ispalindrome(word)

if (ckeck):
  print("Yes")
else:
  print("No")










