import time


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Default values for OneCompiler
arr = [34, 7, 23, 32, 5, 62, 32, 12]

start = time.perf_counter()
sorted_arr = quick_sort(arr)
end = time.perf_counter()

print("Original Array:", arr)
print("Sorted Array:", sorted_arr)
print(f"Execution Time: {end - start:.8f} seconds")

print("\nTime Complexity Summary")
print(f"{'Sorting Algorithm':<18} {'Best Case':<15} {'Average Case':<17} {'Worst Case'}")
print("-" * 70)
print(f"{'Bubble Sort':<18} {'O(n)':<15} {'O(n²)':<17} {'O(n²)'}")
print(f"{'Selection Sort':<18} {'O(n²)':<15} {'O(n²)':<17} {'O(n²)'}")
print(f"{'Insertion Sort':<18} {'O(n)':<15} {'O(n²)':<17} {'O(n²)'}")
print(f"{'Merge Sort':<18} {'O(n log n)':<15} {'O(n log n)':<17} {'O(n log n)'}")
print(f"{'Quick Sort':<18} {'O(n log n)':<15} {'O(n log n)':<17} {'O(n²)'}")
print(f"{'Heap Sort':<18} {'O(n log n)':<15} {'O(n log n)':<17} {'O(n log n)'}")