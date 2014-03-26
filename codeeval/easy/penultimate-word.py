import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  data = test.strip().split(' ')
  if len(data) == 1:
    print data[0]
  else:
    print data[len(data) - 2]
test_cases.close()