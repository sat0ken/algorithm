#!/usr/bin.env python3

from bisect import bisect_left

def binary_search(an_iterable, target):
	index = bisect_left(an_iterable, target)
	if index <= len(an_iterable) and an_iterable[index] == target:
		return True
	return False

a_list = [10, 12, 13, 14, 15, 18, 19]
print(binary_search(a_list, 19))
