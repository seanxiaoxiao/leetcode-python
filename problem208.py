class TrieNode:

    def __init__(self):
        self.next_node = {}
        self.is_ending = False

    def endNode(self):
        self.is_ending = True

    def isEndingNode(self):
        return self.is_ending

    def appendNode(self, c):
        if not self.next_node.get(c):
            self.next_node[c] = TrieNode()

    def hasNode(self, c):
        return self.next_node.get(c) is not None

    def nextNode(self, c):
        return self.next_node.get(c)



class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            node.appendNode(c)
            node = node.next_node(c)
        node.endNode()

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            if not node.hasNode(c):
                return False
            node = node.next_node(c)
        return node.isEndingNode()

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            if not node.hasNode(c):
                return False
            node = node.next_node(c)
        return True