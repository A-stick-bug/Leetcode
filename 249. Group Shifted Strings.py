from collections import defaultdict


# bad question, not well phrased and stuff
def groupStrings(strings):
    def find_pattern(s1, s2):
        return ord(s1) - ord(s2)

    patterns = defaultdict(list)
    for s in strings:
        differences = []
        for i in range(1, len(s)):
            differences.append(find_pattern(s[i], s[i - 1]) % 26)
        patterns[tuple(differences)].append(s)

    return patterns.values()


print(groupStrings(strings=["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
