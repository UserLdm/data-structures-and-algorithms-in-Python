def binary_serach(alist, item):
    """二分查找，递归"""
    n = len(alist)
    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_serach(alist[:mid], item)
        else:
            return binary_serach(alist[mid+1:], item)
    return False

def binary_serach_2(alist, item):
    """二分查找法,非递归"""
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False



if __name__ == "__main__":
    li = [11,22,33,44,55,66,77,88]
    print(binary_serach(li, 55))
    print(binary_serach(li, 100))
    print(binary_serach_2(li, 22))
    print(binary_serach_2(li, 100))
