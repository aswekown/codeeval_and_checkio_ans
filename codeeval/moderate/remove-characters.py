import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    data = map(lambda a: a.strip(),test.strip().split(','))
    print ''.join([i for i in data[0] if i not in data[1]])
test_cases.close()