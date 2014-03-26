import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print sorted(test.strip().split(' '), key = lambda word: len(word), reverse = True)[0]
test_cases.close()