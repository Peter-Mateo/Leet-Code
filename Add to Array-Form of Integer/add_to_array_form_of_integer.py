class Solution(object):
    def addToArrayForm(self, num, k):
        string = ""
        list = []
        for i in range(len(num)):
            string += str(num[i])
        add = str(int(string) + k)
        for numbers in add:
            list.append(numbers)
        return list
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        