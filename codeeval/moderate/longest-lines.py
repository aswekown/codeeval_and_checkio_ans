import sys
test_cases = open(sys.argv[1], 'r')
count = 0
alist = []
for test in test_cases:
    if count == 0:
        end = int(test)
    else:
        alist.append(test)
    count += 1
alist.sort(key = lambda x: len(x), reverse = True)
for i in xrange(0, end):
  print alist[i]
test_cases.close()