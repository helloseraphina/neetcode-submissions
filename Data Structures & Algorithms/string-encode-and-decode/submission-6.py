class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        # loop thru list of input strs
        for s in strs:
            # append s by encoding its length with delimiter
            encode_str += str(len(s)) + "`" + s
        
        return encode_str

    def decode(self, s: str) -> List[str]:
        # init list and pointer i to inidicate position of input str
        # iterate char by char to decode each string
        decode_str, i = [], 0

        while i < len(s):
            # find delimiter with second pointer j
            j = i
            # while char at pointer j is !== delimter 
            # keep incrementing pointer
            while s[j] != '`':
                j += 1
            # length of word is from i to j (the delim)
            # convert to int b/c it is a str
            length = int(s[i:j])
            # j + 1 is first char in string itself
            # go to end of str
            # append to list
            decode_str.append(s[j + 1: j + 1 + length])
            # move pointer i to beginning of next str
            i = j + 1 + length
        
        return decode_str


