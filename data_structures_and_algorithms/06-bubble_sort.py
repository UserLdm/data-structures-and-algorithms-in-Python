def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(n-1):
        count = 0
        for i in range(n-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        if 0 == count:
            return


if __name__ == "__main__":
    li = [1,4,2,3,6,8,9,0]
    print(li)
    bubble_sort(li)
    print(li)
