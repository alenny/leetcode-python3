class TrieNode:
    def __init__(self):
        self.isWordBegin = False
        self.children = dict()


class StreamChecker:

    def __init__(self, words):
        self.stack = []
        self.root = TrieNode()
        for w in words:
            node = self.root
            for ch in w[::-1]:
                if not ch in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.isWordBegin = True

    def query(self, letter: str) -> bool:
        self.stack.append(letter)
        node = self.root
        for i in range(len(self.stack))[::-1]:
            ch = self.stack[i]
            if not ch in node.children:
                return False
            node = node.children[ch]
            if node.isWordBegin:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

obj = StreamChecker(["cd", "f", "kl"])
print(obj.query('a'))
print(obj.query('b'))
print(obj.query('c'))
print(obj.query('d'))
print(obj.query('e'))
print(obj.query('f'))
print(obj.query('g'))
print(obj.query('h'))
print(obj.query('i'))
print(obj.query('j'))
print(obj.query('k'))
print(obj.query('l'))
