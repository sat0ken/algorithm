#!/usr/bin.env python3

def bubble_sort(a_list):
	loop_size = len(a_list) - 1
	for i in range(loop_size):
		no_swap = True
		for j in range(loop_size - i):
			if a_list[j] > a_list[j+1]:
				a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
				no_swap = False
		if no_swap:
			return a_list
	return a_list

a_list = [32, 1, 9, 6]
print(bubble_sort(a_list))
