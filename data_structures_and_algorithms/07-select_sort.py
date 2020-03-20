def select_sort(alist):
    """选择排序
       不稳定
       稳定判断：如果排序后相同元素后面的出现在前面，则不稳定
    """

    n = len(alist)
    for j in range(n-1):
        min = min_index = j
        for i in range(j+1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]


if __name__ == "__main__":
    li = [22,45,3,54,1,67,3]
    print(li)
    select_sort(li)
    print(li)
