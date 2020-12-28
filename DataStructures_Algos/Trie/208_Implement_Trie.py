class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


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
        cur = self.root

        for idx, letter in enumerate(word):

            if letter not in cur.children:
                cur.children[letter] = TrieNode()

            cur = cur.children[letter]

        cur.word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root

        for letter in word:
            if letter not in cur.children:
                return False

            cur = cur.children[letter]

        return cur.word # Check whether the pointer reaches the end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root

        for letter in prefix:
            if letter not in cur.children:
                return False

            cur = cur.children[letter]

        return cur.word or len(cur.children) > 0 # Check whether the pointer reaches the end (when the prefix is
        # actually a word) or the Trie contains that prefix)