import sys
import string
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
   test = test.strip().split(' ')
   for ele in test:
     if ele[0] in string.ascii_lowercase:
       print ele[0].upper() + ele[1:],
     else:
       print ele,
   print 
test_cases.close()
