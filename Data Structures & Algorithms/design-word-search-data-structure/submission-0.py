class Trie:
    def __init__(self):
        self.child=dict()
        self.eow=False

class WordDictionary:

    def __init__(self):
        self.root=Trie()

    def addWord(self, word: str) -> None:
        curr=self.root

        for c in word:
            if c not in curr.child.keys():
                curr.child[c]=Trie()
            
            curr=curr.child[c]

        curr.eow=True
        

    def search(self, word: str) -> bool:
        def searchr(root,string):

            curr=root

            for i,c in enumerate(string):
                if c in curr.child.keys():
                    curr=curr.child[c]
                elif c =='.':
                    for temp in curr.child.values():
                        if searchr(temp,string[i+1:]) == True:
                            return True

                    return False
                else :
                    return False
            
            return curr.eow

        return searchr(self.root,word)

        
