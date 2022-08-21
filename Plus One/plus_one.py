class Solution(object):
    def plusOne(self, digits):
        string = ""
        list = []
        for i in range(len(digits)):
            string += str(digits[i])
        add = str(int(string) + 1)
        for numbers in add:
            list.append(numbers)
        return list
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        