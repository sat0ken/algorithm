#!/usr/bin.env python3

def merge_sort(a_list):
	if (len(a_list) > 1):
		mid = len(a_list) // 2
		left = a_list[:mid]
		right = a_list[mid:]
		merge_sort(left)
		merge_sort(right)

		left_i  = 0
		right_i = 0
		alist_i = 0
		while (
			left_i < len(left) and
			right_i < len(right)
		):
			if left[left_i] <= right[right_i]:
				a_list[alist_i] = left[left_i]
				left_i += 1
			else:
				a_list[alist_i] = right[right_i]
				right_i += 1
			alist_i += 1

		while left_i < len(left):
			a_list[alist_i] = left[left_i]
			left_i += 1
			alist_i += 1

		while right_i < len(right):
			a_list[alist_i] = right[right_i]
			right_i += 1
			alist_i += 1
	return a_list


a_list = [3, 6, 2, 9]
print(merge_sort(a_list))
