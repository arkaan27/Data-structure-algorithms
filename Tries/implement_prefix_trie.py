class TrieNode:
    def __init__(self):
        self.end = False
        self.keys = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, node=None):
        if node is None:
            node = self.root

        if not word:
            node.end = True
        else:
            if word[0] not in node.keys:
                node.keys[word[0]] = TrieNode()
            self.insert(word[1:], node.keys[word[0]])

    def search(self, word, node=None):
        if node is None:
            node = self.root

        if not word:
            return node.end
        elif word[0] not in node.keys:
            return False
        else:
            return self.search(word[1:], node.keys[word[0]])

    def starts_with(self, prefix, node=None):
        if node is None:
            node = self.root

        if not prefix:
            return True
        elif prefix[0] not in node.keys:
            return False
        else:
            return self.starts_with(prefix[1:], node.keys[prefix[0]])


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))  # True
    print(trie.search("app"))  # False
    print(trie.starts_with("app"))  # True
    trie.insert("app")
    print(trie.search("app"))  # True
