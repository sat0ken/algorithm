#!/usr/bin.env python3

def insertion_sort(a_list):
	for i in range(1, len(a_list)):
		value = a_list[i]
		while i > 0 and a_list[i-1] > value:
			a_list[i] = a_list[i-1]
			i = i - 1
		a_list[i] = value
	return a_list

a_list = [6, 5, 8, 2]
print(insertion_sort(a_list))
