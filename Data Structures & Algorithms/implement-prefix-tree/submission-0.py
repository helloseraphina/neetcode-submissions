#create trie node:
class TrieNode:
    def __init__(self):
        
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        # create root TrieNode
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        #current character
        curr = self.root

        # loop thru chars in word
        for char in word:
            # check if it exists in hashmap
            if char not in curr.children:
                # create trie node for that char
                curr.children[char] = TrieNode()
            # move to next character until reach end
            curr = curr.children[char]
        # set end of word = true        
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        # start at root node
        curr = self.root

        for char in word:
            if char not in curr.children:
                # word doesnt exist
                return False
            # move to child node of that char
            curr = curr.children[char]
        
        # it is a word if this returns true
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                # prefix does not exist
                # therefore no word starts w this prefix
                return False
            # shift pointer
            curr = curr.children[char]      
        return True

        