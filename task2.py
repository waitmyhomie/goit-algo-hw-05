def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None 

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return iterations, arr[mid]  

        if arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid] 
            right = mid - 1

    return iterations, upper_bound 


sorted_array = [0.1, 0.5, 1.2, 2.4, 3.8, 4.5, 5.9]
target_value = 2.0

result = binary_search(sorted_array, target_value)
print(result) 
