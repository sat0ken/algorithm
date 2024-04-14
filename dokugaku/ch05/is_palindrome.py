#!/usr/bin.env python3

def is_palindorome(s1):
	s = s1.lower()
	if s == s[::-1]:
		return True
	return False

print(is_palindorome("racecar"))
print(is_palindorome("cat"))
