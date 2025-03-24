class Solution:
    def isValid(self, s:str) -> bool:
        open = ["(", "[", "{"]
        close = [")", "]", "}"]
        stack = []
        if len(s) % 2 != 0:
            return False
        for i in s:
            if i in open:
                stack.append(i)
                # print(stack)
            elif i in close and len(stack) != 0 and close.index(i) == open.index(stack[len(stack) - 1]):
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        return False

print(Solution.isValid(self=Solution, s="([}}])"))
# ){
