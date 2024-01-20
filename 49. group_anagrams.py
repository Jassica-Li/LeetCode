def group_anagrams(strs):
    anagrams_map = {}
    
    for s in strs:
        key = "".join(sorted(s))
        anagrams_map.setdefault(key, []).append(s)
    return list(anagrams_map.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
