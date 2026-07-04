class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        # initialize storage of longest length
        result = 0
        # sliding window has continuously changing left, right pointers
        # start of window 
        l = 0
        
        for r in range(len(s)):
            # if current char already in char set (duplicate)
            # update window
            while s[r] in charSet:
                # remove it then increment l pointer by 1
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            # update longest length
            result = max(result, (r - l) + 1)
        return result