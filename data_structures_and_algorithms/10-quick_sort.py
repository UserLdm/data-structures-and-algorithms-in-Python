def quick_sort(alist, first, last):
    """快速排序 不稳定"""
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        # high左移
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]

    #从循环退出时 low == high
    alist[low] = mid_value

    #对左边的列表执行快速排序
    quick_sort(alist, first, low-1)

    #对右边的列表执行快速排序
    quick_sort(alist, low+1, last)

if __name__ == "__main__":
    li = [11,3,54,23,87,45,6,78,98]
    print(li)
    quick_sort(li, 0, len(li)-1)
    print(li)
