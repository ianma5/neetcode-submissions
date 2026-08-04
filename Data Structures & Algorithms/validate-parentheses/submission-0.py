class Solution:
    def isValid(self, s: str) -> bool:
        # use stack
        stack = []
        hashmap = {
            ')': '(',
            '}':'{',
            ']':'['
        }
        for char in s:
            if char not in hashmap:
                stack.append(char)
            elif not stack or stack.pop() != hashmap[char]:
                return False
            
        if len(stack) == 0:
            return True
        else:
            return False