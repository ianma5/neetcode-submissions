class Solution:
    hashmap = {
        ')': '(',
        '}':'{',
        ']':'['
    }
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for char in s:
            if char not in self.hashmap:
                stack.append(char)
            elif not stack or stack.pop() != self.hashmap[char]:
                return False
            
        if len(stack) == 0:
            return True
        else:
            return False