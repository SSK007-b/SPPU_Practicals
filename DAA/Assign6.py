import time
import random

def partitionD(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quickSortD(arr, low, high):
    if low < high:
        pi = partitionD(arr, low, high)
        quickSortD(arr, low, pi-1)
        quickSortD(arr, pi+1, high)

def partitionR(arr, low, high):
    pivot_index = random.randint(low, high)
    pivot = arr[pivot_index]
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quickSortR(arr, low, high):
    if low < high:
        pi = partitionR(arr, low, high)
        quickSortR(arr, low, pi-1)
        quickSortR(arr, pi+1, high)


if __name__ == "__main__":

    arr = map(int, input("Enter the Number in array in (0, 1, 2) format ").split(','))
    element = list(arr)
    element1 = element
    startD = time.time()
    quickSortD(element, 0, len(element) - 1)
    print("The Sorted Array is ", element)
    print("The Time Required for Deterministic Quick Sort ", time.time()-startD)

    startR = time.time()
    quickSortR(element1, 0, len(element1) - 1)
    print("The Sorted Array is ", element1)
    print("The Time Required for Randomized Quick Sort ", time.time()-startR)