from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #insert sorted first word of strs into dictionary
        # dictionary = {sorted(strs): [word]}
        #for each word from strs, compare with each key in the dictionary and insert into the list for the key that is equal. break
        #create a new key and insert the word into the value
        anagram_map = defaultdict(list)
        for word in strs:
            unique_key = "".join(sorted(word))
            anagram_map[unique_key].append(word)
        return list(anagram_map.values())
