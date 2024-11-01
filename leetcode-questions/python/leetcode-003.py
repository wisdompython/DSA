"""
Longest Substring Without Repeating Characters

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        len_no_repeat = 0
        counter = 0
        this_set = set()
        for i in range(len(s)):
            # as long as this character is in the list
            while s[i] in this_set:
                # remove from the left
                this_set.remove(s[counter])
                counter += 1
            this_set.add(s[i])
            # find the maximum length of the 
            len_no_repeat = max(len_no_repeat, i - counter + 1)
        return len_no_repeat        
                
