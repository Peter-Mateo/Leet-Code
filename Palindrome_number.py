class Solution(object):
    def isPalindrome(self, x):
        start = str(x)
        string = ""
        for letter in start:
            string += letter
        print(string)




        """
        :type x: int
        :rtype: bool
        """
# Test
test = Solution()
test.isPalindrome(123)