def groupAnagrams(strs: list[str]) -> list[list[str]]:
    groups = {}
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        
        if sorted_word not in groups:
            groups[sorted_word] = []
        
        groups[sorted_word].append(word)
    
    return list(groups.values())

strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs1))
strs2 = [""]
print(groupAnagrams(strs2))
strs3 = ["a"]
print(groupAnagrams(strs3))