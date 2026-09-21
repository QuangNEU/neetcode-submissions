from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list = defaultdict(list)
        for word in strs:
            signature = tuple(sorted(word))
            anagram_list[signature].append(word)
        return list(anagram_list.values())