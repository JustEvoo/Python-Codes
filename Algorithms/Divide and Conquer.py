numbers = [38, 27, 43, 3, 9, 82, 10]

def merge_sort(arr):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr

    # 1. Divide: Find the middle and split the array
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # 2. Conquer: Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # 3. Combine: Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    sorted_array = []
    i = j = 0

    # Compare elements from both lists and merge them in order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Append any remaining elements that were left over
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array

print("Sorted:", merge_sort(numbers))