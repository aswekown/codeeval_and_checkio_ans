import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  data = test.strip().split('|')
  data = map(lambda a: [int(i) for i in a], [i for i in map(lambda a: a.strip().split(' '), data)])
  length = len(data[0])
  for i in range(length):
    print data[0][i] * data[1][i],
  print 
test_cases.close()
