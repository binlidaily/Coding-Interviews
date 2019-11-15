def partition(nums, low, high):
    pivot = nums[high]
    pos = high
    while low < high:
        while low < high and nums[low] <= pivot:
            low += 1
        while low < high and nums[high] >= pivot:
            high -= 1
        if low < high:
            nums[high], nums[low] = nums[low], nums[high]
    # 最后这个交换也总忘记
    nums[high], nums[pos] = nums[pos], nums[high]
    return low

def partition1(nums, low, high):
    i = low
    pi = nums[high]
    for j in range(low, high):
        if nums[j] <= pi:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i

def quick_sort1(nums, low, high):
    # 总是缺少这个条件
    if low < high:
        pi = partition(nums, low, high)
        quick_sort(nums, low, pi-1)
        quick_sort(nums, pi+1, high)

def quick_sort(nums, low=0, high=None):
    if high is None:
        high = len(nums) - 1
    def _quick_sort(nums, low, high):
        if low >= high:
            return
        pivot = partition(nums, low, high)
        _quick_sort(nums, low, pivot-1)
        _quick_sort(nums, pivot+1, high)
    return _quick_sort(nums, low, high)

arr = [5, 2, 7, 9, 10 ,3, 4, 1]
low = 0
high = len(arr) - 1
print(arr)
quick_sort(arr, low, high)
print(arr)