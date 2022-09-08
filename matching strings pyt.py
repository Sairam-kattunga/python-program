def two_string(a, b):
  for i in range(min(len(a),len(b))):
    if a[i] == b[i]:
      print(f'{a[i]}')

a = input('enter the first strinng: ')
b = input('enter the second string: ')

two_string(a,b)
