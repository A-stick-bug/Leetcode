# dict values can be lists

def sort_anagram(strs):
    new_strs = {}

    for i in range(len(strs)):
        word = "".join(sorted(strs[i]))

        if word not in new_strs:
            new_strs[word] = [strs[i]]
        else:
            new_strs[word].append(strs[i])

    return list(new_strs.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(sort_anagram(strs))