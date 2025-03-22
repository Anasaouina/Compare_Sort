import time
import numpy as np
import matplotlib.pyplot as plt

# Optimized Bubble Sort for testing large size data 
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  
    return arr  

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr  

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr  
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    merged = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1

    merged.extend(left_half[i:])
    merged.extend(right_half[j:])
    
    return merged  

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)



def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr.copy())  
    return time.time() - start_time


def visualize_sorting_time():
    sizes = np.linspace(100, 1000, 10, dtype=int)  
    bubble_times, insertion_times, merge_times, quick_times = [], [], [], []

    for size in sizes:
        arr = np.random.randint(0, 10000, size)

        bubble_times.append(measure_time(bubble_sort, arr))
        insertion_times.append(measure_time(insertion_sort, arr))
        merge_times.append(measure_time(merge_sort, arr))
        quick_times.append(measure_time(quick_sort, arr))

    plt.figure(figsize=(10, 5))
    plt.plot(sizes, bubble_times, 'r*-', label="Bubble Sort")
    plt.plot(sizes, insertion_times, 'b^-', label="Insertion Sort")
    plt.plot(sizes, merge_times, 'go-', label="Merge Sort")
    plt.plot(sizes, quick_times, 'mD-', label="Quick Sort")

    plt.title("Sorting Algorithm Execution Time Comparison")
    plt.xlabel("Array Size")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    visualize_sorting_time()
