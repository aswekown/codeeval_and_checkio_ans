import sys

tests = open(sys.argv[1], "r")
for test in tests:
  res_list = []
  fun = lambda a: sum([int(i)**2 for i in a])
  count = 123
  is_num = False
  while count != -1:
    temp = str(fun(test.strip()))
    if temp == '1':
      is_num = True
      break
    else:
      if temp in res_list:
        #print temp
        break
      res_list.append(temp)
      test = temp
    count -= 1
    
  #print res_list
  if is_num:
    print 1
  else:
    print 0
tests.close()
