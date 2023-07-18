# def partitionString(s):
#     partitions = [set()]
#     for i in s:
#         if i not in partitions[-1]:
#             partitions[-1].add(i)
#         else:
#             partitions.append({i})
#     return len(partitions)

# don't need to keep track of the partitions
def partitionString(s):
    count = 1
    used = set()
    for i in s:
        if i not in used:
            used.add(i)
        else:
            used = {i}
            count += 1
    return count

print(partitionString("hdklqkcssgxlvehv"))
