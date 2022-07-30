dec = {'a': 100, 'b': 200, 'c': 300}
def is_present(x):
  if x in dec.values():
      print('num is present in the dictionary')
  else:
      print('num is not present in the dictionary')

num=int(input("enter number"))
is_present(num)

