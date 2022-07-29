#!/usr/bin/python3
for ascii_num in range(122, 96, -1):
	if ascii_num % 2 == 1:
		ascii_num = ascii_num - 32
	print("{:c}".format(ascii_num), end='')
