import time

num = [1,5,2,7,3,6,5,8,6,4]

#Divides the numbers into smaller pieces
def test(arr):
	if len(arr) > 1:
		left_side = arr[:len(arr)//2]
		right_side = arr[len(arr)//2:]
			
		left_sort = test(left_side)
		right_sort = test(right_side)
		return merge(left_sort, right_sort)
	else:
		return arr	
		
#Rearranges numbers into order from comparing the left side and right side
def merge(left, right):
	result = []
	i = j = 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	#Cleanup for leftover numbers in list
	result.extend(left[i:])
	result.extend(right[j:])
	return result
	
#Output
print(f"Your numbers: {num}")
for i in range(15):
	dots = "."
	print(f"\rLoading.{dots*(i%3)}", end="")
	time.sleep(0.4)
print()
print(test(num))
