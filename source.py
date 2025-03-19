class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: # If list is empty, returns none
            return ""

        # Sorts lexicographically -> This ensures that first and last strings are the most different
        strs.sort() 
        # First and last elements -> The longest common prefix of these two will be the answer
        first,last=strs[0],strs[-1] 
        i=0
        # Iterate a character by character until a mismatch is found
        while (i<len(first)) and (i<len(last)) and (first[i]==last[i]): # 
            i+=1
        return first[:i]
