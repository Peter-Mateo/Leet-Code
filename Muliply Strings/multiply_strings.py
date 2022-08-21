def convert(number):
        num = int(number)
        return num 
    
class Solution(object):
    def multiply(self, num1, num2):
        num1 = convert(num1)
        num2 = convert(num2)
        math = num1 * num2 
        return str(math)
        
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        