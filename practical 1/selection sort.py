import time


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        minimum = i

        for j in range(i + 1, n):
            if arr[j] < arr[minimum]:
                minimum = j

        arr[i], arr[minimum] = arr[minimum], arr[i]


arr = [64, 25, 12, 22, 11]

start = time.perf_counter()
selection_sort(arr)
end = time.perf_counter()

print("Sorted Array:", arr)
print("Execution Time:", end - start, "seconds")

print("\nTime Complexity")
print("Best Case   : O(n²)")
print("Average Case: O(n²)")
print("Worst Case  : O(n²)")
