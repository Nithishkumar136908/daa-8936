import time

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Input
n = int(input("Enter number of elements: "))
arr = []

print("Enter elements in sorted order:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter element to search: "))

# Time Analysis
start = time.perf_counter()

result = binary_search(arr, key)

end = time.perf_counter()

# Output
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")

print("Execution Time:", end - start, "seconds")
