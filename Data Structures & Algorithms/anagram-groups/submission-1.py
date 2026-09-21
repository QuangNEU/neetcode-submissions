class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list = defaultdict(list)
        
        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char) - ord('a')] += 1
            signature = tuple(count)
            anagram_list[signature].append(word)
        return list(anagram_list.values())