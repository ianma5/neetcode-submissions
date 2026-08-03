class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters = []
        hashmap = {}
        final_list = []

        for word in strs:
            letter_list = [0] * 26
            for char in word:
                letter_list[ord(char) - ord('a')] += 1
            letter_list = tuple(letter_list)
            if letter_list not in hashmap:
                hashmap[letter_list] = []
            hashmap[letter_list].append(word)

        return list(hashmap.values())