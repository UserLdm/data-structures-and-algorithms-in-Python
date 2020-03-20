def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n // 2

    # gap变化到0之前，插入算法执行的次数
    while gap > 0:
        #插入算法，与普通的插入算法的区别就是gap步长
        for j in range(gap, n):
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2

if __name__ == "__main__":
    li = [32,45,31,34,5,67,3,54] 
    print(li)
    shell_sort(li)
    print(li)
