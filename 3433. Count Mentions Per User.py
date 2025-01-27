# https://leetcode.com/problems/count-mentions-per-user
# just implement it
# be careful about sorting the events, we need to tiebreak same times
# by doing OFFLINE commands first

def countMentions(numberOfUsers: int, events: list[list[str]]) -> list[int]:
    events.sort(key=lambda x: (int(x[1]), x[0] == "MESSAGE"))
    n = numberOfUsers
    freq = [0] * n

    nxt_online = [-1] * n

    for t, time, s in events:
        if t == "MESSAGE":
            if s == "ALL":
                for i in range(n):
                    freq[i] += 1
            elif s == "HERE":
                for i in range(n):
                    if nxt_online[i] <= int(time):
                        freq[i] += 1
            else:
                for u_id in s.split():
                    u_id = int(u_id[2:])
                    freq[u_id] += 1

        else:
            nxt_online[int(s)] = int(time) + 60

    return freq


print(countMentions(3, [["MESSAGE", "2", "HERE"], ["OFFLINE", "2", "1"], ["OFFLINE", "1", "0"],
                        ["MESSAGE", "61", "HERE"]]))
print(countMentions(numberOfUsers=2,
                    events=[["MESSAGE", "10", "id1 id0"], ["OFFLINE", "11", "0"], ["MESSAGE", "71", "HERE"]]))
print(countMentions(numberOfUsers=2,
                    events=[["MESSAGE", "10", "id1 id0"], ["OFFLINE", "11", "0"], ["MESSAGE", "12", "ALL"]]))
print(countMentions(numberOfUsers=2, events=[["OFFLINE", "10", "0"], ["MESSAGE", "12", "HERE"]]))
