import sys
tests = open(sys.argv[1], "r")
for test in tests:
  string = test.strip().split(',')[0]
  char = test.strip().split(',')[1]
  length = len(string)
  index = -1
  for i in xrange(length):
    if string[i] == char:
      index = i
  print index
tests.close()
