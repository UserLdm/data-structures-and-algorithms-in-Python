def insert_sort(alist):
    """插入排序 稳定"""
    n = len(alist)
    for j in range(1, n):
        # i代表内层循环起始值
        i = j
        # 执行从右边的无序序列中取出第一个元素，即第i位置元素，然后插入前面的正确位置中

        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i-=1
            else:
                break

if __name__ == "__main__":
    li = [11,34,23,67,45,98,34]
    print(li)
    insert_sort(li)
    print(li)
