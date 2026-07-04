# from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_dict = defaultdict(list) # mapping char count to list of anagrams
        #defaultdict if you try to access a key that doesn't exist, it automatically creates that key with a default value - in this case, an empty list.

        # go thru each word in str list
        for s in strs:
            count = [0] * 26 # one zero for each char of alphabet
            # go thru each char in each word
            for char in s:
                # get ascii value of curr character c and substract ascii from lowercase a
                # to get char indexes
                # increment by 1 to count
                count[ord(char) - ord('a')] += 1
            
            # change to tuple bc list cannot be keys
            # tuple immutable
            char_dict[tuple(count)].append(s)
        
        # return anagrams grouped together without char key count
        # return as list
        return list(char_dict.values())
