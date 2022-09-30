class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Declaring the String
        so_far = ''
        finish = 0
        next_seq = 0
        # For loop to start 
        for letter in s:
            # Check if the letter is in the string 
            if letter in so_far:
                so_far = ''
                if finish == 0:
                    finish = len(so_far)
                else:
                    next_seq = len(so_far)
            # Add the letter to the new 
            else:
                so_far += letter
        if finish > next_seq:
            return finish
        else: 
            return next_seq
                
        # Create a for loop that loops through each letter in so_far to check against the current letter 
        
        """
        :type s: str
        :rtype: int
        """
test = Solution()
test.lengthOfLongestSubstring('abcabcbb')
