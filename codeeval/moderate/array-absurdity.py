import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  data = test.strip().split(';')
  sum_them = sum(xrange(int(data[0]) - 1))
  print sum(map(int, data[1].split(','))) - sum_them
test_cases.close()
