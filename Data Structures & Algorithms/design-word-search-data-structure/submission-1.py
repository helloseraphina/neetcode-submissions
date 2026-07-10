# init trienode
class TrieNode:
    def __init__(self):
        self.children = {} # populate with chars eg a: TrieNode
        self.word = False # mark end of word

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # set current to root
        cur = self.root

        # check if char in word
        for c in word:
            if c not in cur.children:
                # insert new trienode corresponding to char c
                cur.children[c] = TrieNode()
            # update pointer to char if it already existed
            cur = cur.children[c]
        
        cur.word = True

        

    def search(self, word: str) -> bool:
        # recursive
        def dfs(j, root):
            cur = root

            # loop thru words
            for i in range(j, len(word)):
                # character of word in index i
                c = word[i]

                if c == ".":
                    # recursive function
                    for child in cur.children.values():
                        # pass in starting index = j
                        # current node = child
                        if dfs(i + 1, child):
                            return True
                    return False
                
                else:
                    # regular character
                    # if it doesnt exist
                    if c not in cur.children:
                        # doesnt exist
                        return False
                    # does exist
                    cur = cur.children[c]
            return cur.word

        # call dfs
        # start at 0, and start at root
        return dfs(0, self.root)
            
