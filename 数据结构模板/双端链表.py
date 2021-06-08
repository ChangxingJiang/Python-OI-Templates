class DoublyLinkedList:
    """双端链表"""

    class _Node:
        __slots__ = "val", "prev", "next"

        def __init__(self, val, prev, next):
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header.next = self._trailer
        self._trailer.prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def __bool__(self):
        return self._size > 0

    def first(self):
        if not self:
            raise KeyError("empty deque")
        return self._header.next

    def last(self):
        if not self:
            raise KeyError("empty deque")
        return self._trailer.prev

    def _insert_between(self, val, before, after):
        newest = self._Node(val, before, after)
        before.next = newest
        after.prev = newest
        self._size += 1
        return newest

    def delete_node(self, node):
        before = node.prev
        after = node.next
        before.next = after
        after.prev = before
        self._size -= 1
        return node

    def insert_first(self, val):
        return self._insert_between(val, self._header, self._header.next)

    def insert_last(self, val):
        return self._insert_between(val, self._trailer.prev, self._trailer)

    def delete_first(self):
        if not self:
            raise KeyError("empty deque")
        return self.delete_node(self._header.next)

    def delete_last(self):
        if not self:
            raise KeyError("empty deque")
        return self.delete_node(self._trailer.prev)

    def __repr__(self):
        ans = []
        node = self._header.next
        while node.next:
            ans.append(str(node.val))
            node = node.next
        return "deque:" + "<->".join(ans)
