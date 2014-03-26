import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test.strip().split(',')[0].strip().endswith(test.strip().split(',')[1].strip()):
        print 1
    else:
        print 0
test_cases.close()