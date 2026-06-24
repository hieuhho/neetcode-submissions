
class Trie():
    def __init__(self):
        self.child = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Trie()


    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter not in current.child:
                current.child[letter] = Trie()
            current = current.child[letter]
        current.end = True


    def search(self, word: str) -> bool:
        current = self.root
        for letter in word:
            if letter not in current.child:
                return False
            current = current.child[letter]
        return current.end


    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for letter in prefix:
            if letter not in current.child:
                return False
            current = current.child[letter]
        return True
