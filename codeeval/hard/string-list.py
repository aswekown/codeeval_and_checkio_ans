import sys
import itertools

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
   times = int(test.strip().split(',')[0])
   data = test.strip().split(',')[1]
   alist = []
   res = list(set([i for i in itertools.product(data, repeat = times)]))
   res.sort()
   #print res
   for i in res:
     alist.append(reduce(lambda x,y: x+y, [j for j in i]))
   #print alist
   print ','.join(alist)
   
test_cases.close()