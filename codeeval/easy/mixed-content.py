from sys import argv
# we can not use isdigit function beacuse it cannot return true in '-1'.isdigit()
tests = open(argv[1], "r")
for test in tests:
	test = test.strip().split(',')
	num_list = []
	word_list = []
	for i in test:
		try:
			num_list.append(int(i))
		except ValueError:
			word_list.append(i)
	words = ''
	nums = ''
	if word_list and num_list:
		res = ','.join([word for word in word_list]) + '|' + ','.join([str(num) for num in num_list])
	elif word_list:
		res = ','.join([word for word in word_list])
	elif num_list:
		res = ','.join([str(num) for num in num_list])
	print res
tests.close()
