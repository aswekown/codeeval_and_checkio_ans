import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  res = ''
  data = test.strip().split(' ')
  if '+' in data[1]:
    operator_index = data[1].index('+')
    res = int(data[0][0:operator_index],10) + int(data[0][operator_index:],10)
  elif '-' in data[1]:
    operator_index = data[1].index('-')
    res = int(data[0][0:operator_index],10) - int(data[0][operator_index:],10)
  print res
test_cases.close()
