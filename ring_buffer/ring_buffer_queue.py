
from doubly_linked_list import DoublyLinkedList

from my_queue import MyQueue


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.orderQueue = MyQueue()

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
            self.orderQueue.enqueue(item)
        else:
            self.orderQueue.enqueue(item)
            oldest_item = self.orderQueue.dequeue()
            for i, v in enumerate(self.storage):
                if v == oldest_item:
                    self.storage[i] = item

    def get(self):
        return self.storage

    def __str__(self):
        output = '['
        for i in self.storage:
            output += ', ' + i
        return output + ']'

# buffer = RingBuffer(3)
#
# buffer.append('a')
# buffer.append('b')
# buffer.append('c')
# buffer.append('d')
# buffer.append('e')
# print(buffer)

