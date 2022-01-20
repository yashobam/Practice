global odd
global even
even=set()
odd=set()
def func(arr):
	global odd
	global even
	for i in range(len(arr)):
		if arr[i]%2==0:
			even.add(i)
		else:
			odd.add(i)