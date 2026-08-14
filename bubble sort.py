import time 
 
def bubble_sort(arr): 
    n = len(arr) 
 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
 
n = int(input("Enter number of elements: ")) 
 
arr = [] 
 
for i in range(n): 
    arr.append(int(input(f"Enter element {i+1}: "))) 
 
start = time.perf_counter() 
 
bubble_sort(arr) 
 
end = time.perf_counter() 
 
print("\nSorted Array:", arr) 
print("Execution Time:", end-start, "seconds") 
 
print("\nTime Complexity") 
print("Best Case   : O(n)") 
print("Average Case: O(n²)") 
print("Worst Case  : O(n²)")  