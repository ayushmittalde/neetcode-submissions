class TrieNode:
    def __init__(self):
        self.child=dict()
        self.eow=False

class PrefixTree:

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        temp=self.root
        for c in word:
            if c not in temp.child.keys():
                temp.child[c]=TrieNode()

            temp=temp.child[c]

        temp.eow=True




    def search(self, word: str) -> bool:
        curr=self.root

        for c in word:
            if c not in curr.child.keys():
                return False
            else :
                curr=curr.child[c]

        return curr.eow

    def startsWith(self, prefix: str) -> bool:

        curr=self.root

        for c in prefix:
            if c not in curr.child.keys():
                return False

            curr=curr.child[c]

        return True

        
        