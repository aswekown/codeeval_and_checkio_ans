import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  data = map(lambda a: int(a.strip()), test.split(','))
  length = len(data)
  alist = [data[i:j+1] for i in xrange(length) for j in xrange(i, length)]
  print max(map(lambda a: sum(a), alist))
test_cases.close()
