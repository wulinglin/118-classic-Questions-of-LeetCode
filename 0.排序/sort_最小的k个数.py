"""
1、k轮冒泡排序：O(KN)
快排：O(nlogn)
快排中的Partition思想:O(N):因为我们是要找下标为k的元素，总之可以看作每次调用 partition 遍历的元素数目都是上一次遍历的 1/2，因此时间复杂度是 N + N/2 + N/4 + … + N/N = 2N, 因此时间复杂度是 O(N)
堆排序:O(nlogN):每次新人与堆顶PK，PK结束之后维护候选人重新为大顶堆,每次是logK。
数据很大的时候选择堆排序！：堆排序方法将全部排序降为部分排序，这在海量数据中查找topK中是很有用的，当数据是增量式，或者无法全部加载进内存中时，只开辟一小部分空间存储k个数字还是可以实现的。
"""

# 堆
"""
最大堆
A:数组 
i:父节点的index
size:堆的大小

详细：https://www.cnblogs.com/chengxiao/p/6129630.html
实现：https://zhuanlan.zhihu.com/p/77527032
a.将无需序列构建成一个堆，根据升序降序需求选择大顶堆或小顶堆;
b.将堆顶元素与末尾元素交换，将最大元素"沉"到数组末端;
c.重新调整结构，使其满足堆定义，然后继续交换堆顶元素与当前末尾元素，反复执行调整+交换步骤，直到整个序列有序。
"""


def heap_adjust(A, i, size):
    left = 2 * i + 1
    right = 2 * i + 2
    max_index = i
    if left < size and A[left] > A[max_index]:
        max_index = left
    if right < size and A[right] > A[max_index]:
        max_index = right
    if max_index != i:
        A[max_index], A[i] = A[i], A[max_index]
        heap_adjust(A, max_index, size)  # 以替换的点为父节点，再调整所在的堆


def build_heap(A, size):
    for i in range(size // 2, -1, -1):
        heap_adjust(A, i, size)


def heap_sort(A):
    size = len(A)
    build_heap(A, size)  # 初始化堆
    for i in range(len(A) - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heap_adjust(A, 0, i)
    return A


nums = [2, 7, 8, 1, 5, 4, 3, 9, 6]
print(heap_sort(nums))

""" 建立最小堆"""


def heap_adjust(A, i, size):
    left = 2 * i + 1
    right = 2 * i + 2
    min_index = i
    if left < size and A[left] < A[min_index]:
        min_index = left
    if right < size and A[right] < A[min_index]:
        min_index = right
    if min_index != i:
        temp = A[i]
        A[i] = A[min_index]
        A[min_index] = temp
        heap_adjust(A, min_index, size)
    return A


def build_heap(A, size):
    for i in range(size // 2, -1, -1):
        heap_adjust(A, i, size)
    return A


def heap_sort(A):
    size = len(A)
    A = build_heap(A, size)
    for i in range(len(A) - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        A = heap_adjust(A, 0, i)
    return A


# 这里假设k = 3 取top 3的数字
nums = [2, 7, 8, 1, 5, 4, 3, 9, 6]
# print(heap_sort(nums))
b = build_heap(nums[:3], 3)
# 从k+1开始，依次比较，然后替换
for i in range(3, len(nums)):
    if nums[i] > b[0]:
        temp = nums[i]
        nums[i] = b[0]
        b[0] = temp
        b = heap_adjust(b, 0, 3)
    print(i, nums[:i + 1], b)
print(b[0])
