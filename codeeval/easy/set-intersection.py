import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  data = list(reduce(lambda a,b: a & b, map(set,\
   map(lambda string: string.split(','),\
   	test.strip().split(';')))))
  data.sort()
  print ','.join(data)
test_cases.close()
