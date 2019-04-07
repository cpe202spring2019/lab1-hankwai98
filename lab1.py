
def max_list_iter(int_list):  # must use iteration not recursion
	"""finds the max of a list of numbers and returns the value (not the index)
	If int_list is empty, returns None. If list is None, raises ValueError"""
	if int_list is None:
		raise ValueError
	elif (len(int_list) == 0):
		return None
	else:
		max = int_list[0]
		for larger in int_list:
			if larger > max:
				max = larger
		return max

def reverse_rec(int_list):   # must use recursion
	if int_list is None:
		raise ValueError
	if len(int_list) <= 1:
		return int_list
	else:
		return reverse_rec(int_list[1:])+[int_list[0]]

def bin_search(target, low, high, int_list):  # must use recursion
	mid = (low + high)//2

	if int_list is None:
		raise ValueError
	elif (len(int_list) == 0):
		return None
	elif (int_list[mid] == target):
		return mid
	elif (int_list[mid] < target):
		return bin_search(target, mid + 1, high, int_list)
	elif (int_list[mid] > target):
		return bin_search(target, low, mid -1, int_list)

