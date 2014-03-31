import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  data = test.strip().split(",")
  alist = []
  for i in data:
    if i not in alist:
      alist.append(i)
  print ",".join(alist)
test_cases.close()
