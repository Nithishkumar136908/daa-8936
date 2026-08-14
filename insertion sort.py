import time 
 
def insertion_sort(arr): 
 
    for i in range(1, len(arr)): 
 
        key = arr[i] 
 
        j = i - 1 
 
        while j >= 0 and key < arr[j]: 
            arr[j+1] = arr[j] 
            j -= 1 
 
        arr[j+1] = key 
 
n = int(input("Enter number of elements: ")) 
 
arr = [] 
 
for i in range(n): 
    arr.append(int(input(f"Enter element {i+1}: "))) 
 
start = time.perf_counter() 
 
insertion_sort(arr) 
 
end = time.perf_counter() 
 
print("\nSorted Array:", arr) 
print("Execution Time:", end-start, "seconds")
print("\nTime Complexity") 
print("Best Case   : O(n)") 
print("Average Case: O(n²)") 
print("Worst Case  : O(n²)") 