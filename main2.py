def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if arr[mid] == x:
            return iterations, arr[mid]

        elif arr[mid] < x:
            low = mid + 1

        else:
            high = mid - 1
            upper_bound = arr[mid]

    if upper_bound is None and low < len(arr):
        upper_bound = arr[low]

    return iterations, upper_bound


arr = [2.2, 3.5, 4, 10.77, 40]
x = 5.8
result = binary_search(arr, x)

if result[1] is not None:
    print(f"Iterations: {result[0]}, Upper Bound: {result[1]}")
else:
    print(f"Iterations: {result[0]}, No upper bound found")
