import time

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Input
n = int(input("Enter number of elements: "))
arr = []

print("Enter elements:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter element to search: "))

# Time Analysis
start = time.perf_counter()

result = linear_search(arr, key)

end = time.perf_counter()

# Output
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")

print("Execution Time:", end - start, "seconds")
