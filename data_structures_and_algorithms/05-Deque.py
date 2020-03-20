#coding:utf-8

class Queue(object):
    """队列"""
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """往队列中添加一个item元素"""
        self.__list.insert(0,item)

    def add_rear(self,item):
        """在队列的尾部添加一个元素"""
        self.__list.append(item)

    def pop_front(self):
        """从队头删除一个元素"""
        return self.__list.pop(0)

    def pop_rear(self):
        """从队头删除一个元素"""
        return self.__list.pop()

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)


if __name__ == "__main__":
    s = Queue()
    s.add_front(2)
    s.add_front(3)
    s.add_front(4)
    s.add_front(5)
    s.add_rear(6)
    s.add_rear(7)
    s.add_rear(8)
    s.add_rear(9)
    print(s.pop_front())
    print(s.pop_front())
    print(s.pop_front())
    print(s.pop_front())
    print(s.pop_rear())
    print(s.pop_rear())
    print(s.pop_rear())
    print(s.pop_rear())

