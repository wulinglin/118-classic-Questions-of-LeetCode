# 快速排序函数
def quickSort(arr, low, high):
    def partition(arr, low, high):
        i = (low - 1)  # 最小元素索引
        pivot = arr[high]
        print(11111, arr, pivot, low, high)
        for j in range(low, high):
            # 当前元素小于或等于 pivot
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        print(22222, arr)
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        print(22222, arr)
        return (i + 1)

    if low < high:
        pi = partition(arr, low, high)
        print(33333, pi)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("quickSort排序后的数组:", arr)
