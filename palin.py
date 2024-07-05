
def isPalindrome(s):
	rev = ''.join(reversed(s))
	if (s == rev):
		return True
	return False
s = "malayalam"
result = isPalindrome(s)

if (result):
	print("Yes")
else:
	print("No")
