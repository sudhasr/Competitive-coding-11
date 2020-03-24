class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        #symbols = ["+", "-", "*", "/"]
        stack = []
        #print(6/-132)
        #res = 0
        # ["2", "1", "+", "3", "*"]
        for i in tokens:
            #if i in symbols:
                if i == "+":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    res = self.addition(num1, num2)
                    stack.append(res)
                elif i == "-":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    res = self.subt(num1, num2)
                    stack.append(res)
                elif i == "*":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    res = self.prod(num1, num2)
                    stack.append(res)
                elif i == "/":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    res = self.divi(num1, num2)     
                    stack.append(res)
                else:
                    stack.append(int(i)) #[9]
                #print(stack)
        return stack.pop()
    def addition(self,num1, num2):
        return num1 + num2
    def subt(self,num1, num2):
        return num1 - num2
    def prod(self,num1, num2):
        return num1 * num2
    def divi(self,num1, num2):
        return int(float(num1) / num2)