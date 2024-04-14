#!/usr/bin.env python3

def binary_search(a_list, n):
	first = 0
	last = len(a_list) - 1
	while last >= first:
		mid = (first + last) // 2
		if a_list[mid] == n:
			return True
		else:
			if n < a_list[mid]:
				last = mid - 1
			else:
				first = mid + 1
	return False

a_list = [10, 12, 13, 14, 15, 18, 19]
print(binary_search(a_list, 19))
