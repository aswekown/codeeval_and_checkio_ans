import sys
test_cases = open(sys.argv[1], 'r')
numbers_str = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
           'eight', 'nine']
numbers = xrange(0,10)
adict = dict(zip(numbers_str, numbers))
#print adict
for test in test_cases:
  print ''.join([str(adict[i]) for i in test.strip().split(';')])
test_cases.close()
