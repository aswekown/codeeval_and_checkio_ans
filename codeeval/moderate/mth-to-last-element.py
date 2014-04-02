import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  data = test.strip().split(' ')
  index = int(data[-1])
  try:
    print data[-index-1]
  except:
    pass
test_cases.close()
