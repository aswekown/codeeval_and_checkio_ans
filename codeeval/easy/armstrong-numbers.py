import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  test = test.strip()
  #print test
  num = int(test)
  #print num
  length = len(test)
  sumit = 0
  for i in test:
    #print i
    sumit += (int(i) ** length)
  if sumit == num:
    print True
  else:
    print False
test_cases.close()
