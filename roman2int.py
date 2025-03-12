class Solution:
    def romanToInt(self, s:str) -> int:
        value = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        stack = []
        result = 0
        for i, key in zip(range(len(s)), s):
            stack.append(value[key])
            try:
                if stack[i - 1] >= stack[i]:
                    result += stack[i]
                else:
                    result += (stack[i - 1] * - 1) + stack[i] - stack[i - 1]
            except IndexError:
                print(IndexError)
        return result    
