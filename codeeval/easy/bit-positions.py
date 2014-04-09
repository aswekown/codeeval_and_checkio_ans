import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  data = test.strip().split(',')
  num = bin(int(data[0])).lstrip('0b')[-1::-1]
  index_one = int(data[1])
  index_two = int(data[2])
  if num[index_one - 1] == num[index_two - 1]:
    print 'true'
  else:
    print 'false'
test_cases.close()
