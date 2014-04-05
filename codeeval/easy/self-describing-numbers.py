import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  test = test.strip()
  length = len(test)
  all_match = True
  for i in xrange(length):
    if int(test[i]) != test.count(str(i)):
      all_match = False
      break
  if all_match:
    print 1
  else:
    print 0
test_cases.close()
