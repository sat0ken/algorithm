#!/usr/bin/env python3

def factorial(n):
	print(n)
	if n == 10:
		return 1
	return n * factorial(n + 1)

factorial(1)
