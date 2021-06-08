class Trie:
    class _Node:
        __slots__ = "value", "weight", "children"

        def __init__(self):
            self.value = None
            self.weight = 0
            self.children = {}

        def __contains__(self, ch):
            return ch in self.children

        def __getitem__(self, ch):
            return self.children[ch]

        def __setitem__(self, ch, value):
            self.children[ch] = value

    def __init__(self):
        self.root = self._Node()

    def add(self, word):
        """向字典树中添加词语:True=成功添加;False=已有该词"""
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = self._Node()
            node.weight += 1
            node = node[ch]
        if node.value is None:
            node.value = word
            return True
        else:
            return False

    def remove(self, word, weight=1):
        """从字典树中移除词数(并不是真的删除，而是移除权重):True=成功移除;False=没有该词"""
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node.weight -= weight
            node = node[ch]

    def __contains__(self, word):
        """判断词语是否存在"""
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return node.value == word

    def search(self, string):
        """寻找字符串中从头开始的第1个词语（如果没有找到则返回None）"""
        node = self.root
        for ch in string:
            if ch not in node:
                return None
            node = node[ch]
            if node.value is not None:
                return node.value

    def start_with(self, string):
        """寻找字符串中是否有以string开头的"""
        node = self.root
        for ch in string:
            if ch not in node:
                return False
            node = node[ch]
        return True
