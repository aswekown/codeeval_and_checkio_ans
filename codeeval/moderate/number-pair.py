import sys
from itertools import combinations

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    data = int(test.strip().split(';')[1])
    num_list = test.strip().split(';')[0].split(',')
    num_list = map(int, num_list)
    #print num_list
    pair_iter = combinations(num_list, 2)
    has_one = False
    res_list = []
    for i in pair_iter:
      if sum(i) == data:
        has_one = True
        res_list.append(str(i[0]) + "," + str(i[1]))
      if i[0] >= data:
        break
    if has_one == False:
      print 'NULL'
    else:
      print ';'.join(res_list)
test_cases.close()
