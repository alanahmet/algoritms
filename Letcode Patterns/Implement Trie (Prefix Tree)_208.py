class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node:
                node[w] = {}
            node = node[w]
        node['end'] = True

    def search(self, word: str) -> bool:
        node = self.find(word)
        return node is not None and 'end' in node

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix) is not None

    def find(self, prefix: str) -> dict:
        node = self.root
        for c in prefix:
            if c not in node:
                return None
            node = node[c]
        return node
