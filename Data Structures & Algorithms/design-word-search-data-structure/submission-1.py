class TrieNode:
    
    def __init__(self):
        self.child = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        tmp = self.root
        for c in word:
            if c not in tmp.child:
                tmp.child[c] = TrieNode()
            tmp = tmp.child[c]
        tmp.end = True


    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.child.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.child:
                        return False
                    cur = cur.child[c]
            return cur.end
        return dfs(0, self.root)