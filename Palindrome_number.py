class Solution(object):
    def isPalindrome(self, x):
        # Sets the integer to a string
        start = list(str(x))
        # Turns it backwards
        done = list(reversed(start))
        # Check
        if start == done:
            return True
        else:
            return False
        """
        :type x: int
        :rtype: bool
        """
# Test
test = Solution()
test.isPalindrome(12121)