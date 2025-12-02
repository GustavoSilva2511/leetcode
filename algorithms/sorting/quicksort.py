def quicksort(arr, left, right):
    if left < right:
        pi = partition(arr, left, right)
        quicksort(arr, left, pi-1)
        quicksort(arr, pi+1, right)

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]


    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i + 1


arr = [1, 3, 4, 2, 7, 8, 6, 5]
quicksort(arr, 0, len(arr) - 1 )
print(arr)

