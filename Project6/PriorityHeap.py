"""
PROJECT 6 - Priority Queues and Heaps
Name: Justin Vesche
"""


class Node:
    """
    This class represents a node object with k (key) and v (value)
    Node definition should not be changed in any way
    """

    def __init__(self, k, v):
        """
        Initializes node
        :param k: key to be stored in the node
        :param v: value to be stored in the node
        """
        self.key = k
        self.value = v

    def __lt__(self, other):
        """
        Less than comparator
        :param other: second node to be compared to
        :return: True if the node is less than other, False otherwise
        """
        return self.key < other.key or (self.key == other.key and self.value < other.value)

    def __gt__(self, other):
        """
        Greater than comparator
        :param other: second node to be compared to
        :return: True if the node is greater than other, False otherwise
        """
        return self.key > other.key or (self.key == other.key and self.value > other.value)

    def __eq__(self, other):
        """
        Equality comparator
        :param other: second node to be compared to
        :return: True if the nodes are equal, False otherwise
        """
        return self.key == other.key and self.value == other.value

    def __str__(self):
        """
        Converts node to a string
        :return: string representation of node
        """
        return '({0},{1})'.format(self.key, self.value)

    __repr__ = __str__


class PriorityHeap:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """

    def __init__(self, is_min=True):
        """
        Initializes the priority heap
        """
        self._data = []
        self.min = is_min

    def __str__(self):
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self._data)

    def __len__(self):
        """
        Length override function
        :return: Length of the data inside the heap
        """
        return len(self._data)

    __repr__ = __str__

#   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Modify below this line

    def empty(self):
        """
        check if heap is empty
        :return: True if empty, else false
        """
        return not bool(len(self._data))

    def top(self):
        """
        Get the top of the heap
        :return: top of heap
        """
        if self.empty():
            return None
        else:
            return self._data[0].value

    def push(self, key, val):
        """
        Push a value into the heap
        :return: None
        """
        inserted = Node(key, val)
        if self.empty():
            self._data.append(inserted)
            return None
        else:
            self._data.append(inserted)
            index = len(self) - 1
            self.percolate_up(index)
            return None

    def pop(self):
        """
        Remove the top element of the heap
        :return: The node
        """
        if self.empty():
            return None
        elif len(self) == 1:
            return self._data.pop()
        else:
            end = len(self) - 1
            self._data[0], self._data[end] = self._data[end], self._data[0]
            prev = self._data.pop()
            self.percolate_down(0)
            return prev


    def min_child(self, index):
        """
        Find the min child of the current parent
        :return: The min child
        """
        left = 2 * index + 1
        if len(self) <= left:
            return None
        the_min = left
        right = index * 2 + 2
        if len(self) > right:
            if self._data[right] < self._data[left]:
                the_min = right
            elif self._data[right] == self._data[left]:
                the_min = right
        return the_min

    def max_child(self, index):
        """
        Find the max child of the the given parent
        :return: The max child
        """
        left = 2 * index + 1
        if len(self) <= left:
            return None
        the_max = left
        right = index * 2 + 2
        if len(self) > right:
            if self._data[right] > self._data[left]:
                the_max = right
            elif self._data[right] == self._data[left]:
                the_max = right
        return the_max


    def percolate_up(self, index):
        """
        Bubble up the heap, swapping any out of order elements
        on the way up from the index
        :return: None
        """
        parent = int((index - 1) // 2)
        if self.min:
            if index > 0 and self._data[index] < self._data[parent]:
                self._data[index], self._data[parent] = self._data[parent], self._data[index]
                self.percolate_up(parent)
        else:
            if index > 0 and self._data[index] > self._data[parent]:
                self._data[index], self._data[parent] = self._data[parent], self._data[index]
                self.percolate_up(parent)

    def percolate_down(self, index):
        """
        Drop down heap, swapping any out of order elements
        :return: None
        """
        left = index * 2 + 1
        if len(self) > left:
            set_child = left
            if self.min:
                set_child = self.min_child(index)
                if self._data[set_child] < self._data[index]:
                    self._data[index], self._data[set_child] = self._data[set_child], self._data[index]
                    self.percolate_down(set_child)
            else:
                set_child = self.max_child(index)
                if self._data[set_child] > self._data[index]:
                    self._data[index], self._data[set_child] = self._data[set_child], self._data[index]
                    self.percolate_down(set_child)



def heap_sort(array):
    """
    Place the array into a Max Heap. Pop each element of the
    max heap and place the popped element into the end
    of a new list.
    :return: A sorted list.
    """
    max_heap = PriorityHeap(False)
    list_return = array
    for val in array:
        max_heap.push(val, val)
    count = len(array) - 1
    while not max_heap.empty():
        into = max_heap.pop()
        list_return[count] = into.key
        count -= 1
    return list_return



def current_medians(values):
    """
    Use max and min heap to find the median of the current list.
    Places half of the list in a max heap and the other half in a min
    heap, with the smallest half being in the max heap.
    :return: The a list with the median of each current index of the array.
    """
    order_of_medians = []
    min_heap = PriorityHeap()
    max_heap = PriorityHeap(False)
    for val in values:
        if max_heap.empty():
            max_heap.push(val, val)
            order_of_medians.append(val)
        elif min_heap.empty():
            max_heap.push(val, val)
            temp = max_heap.pop()
            min_heap.push(temp.key, temp.key)
            order_of_medians.append((min_heap.top() + max_heap.top()) / 2)
        else:
            if len(max_heap) == len(min_heap):
                if val > min_heap.top():
                    min_heap.push(val, val)
                    order_of_medians.append(min_heap.top())
                else:
                    max_heap.push(val, val)
                    order_of_medians.append(max_heap.top())
            elif val > min_heap.top():
                min_heap.push(val, val)
                if len(min_heap) - len(max_heap) > 1:
                    temp = min_heap.pop()
                    max_heap.push(temp.key, temp.key)
                    order_of_medians.append((min_heap.top() + max_heap.top()) / 2)
                elif len(max_heap) == len(min_heap):
                    order_of_medians.append((min_heap.top() + max_heap.top()) / 2)
                else:
                    order_of_medians.append(min_heap.top())
            else:
                max_heap.push(val, val)
                if len(max_heap) - len(min_heap) > 1:
                    temp = max_heap.pop()
                    min_heap.push(temp.key, temp.key)
                    order_of_medians.append((min_heap.top() + max_heap.top()) / 2)
                elif len(max_heap) == len(min_heap):
                    order_of_medians.append((min_heap.top() + max_heap.top()) / 2)
                else:
                    order_of_medians.append(max_heap.top())
    return order_of_medians
