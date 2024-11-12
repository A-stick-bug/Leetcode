# https://leetcode.com/problems/most-beautiful-item-for-each-query
# Beginner offline queries question
# note: binary search is also a valid approach

def maximumBeauty(items: list[list[int]], queries: list[int]) -> list[int]:
    n = len(items)
    q = len(queries)
    items.sort(key=lambda x: x[0])  # sort by price

    queries = [(val, i) for i, val in enumerate(queries)]
    queries.sort(key=lambda x: x[0])  # sort by price

    max_beauty = 0
    idx = 0
    ans = [-1] * q

    # consider beauty of all items with (price <= what the current query allows)
    for max_price, q_idx in queries:
        while idx < n and items[idx][0] <= max_price:
            max_beauty = max(max_beauty, items[idx][1])
            idx += 1
        ans[q_idx] = max_beauty

    return ans


print(maximumBeauty(items=[[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], queries=[1, 2, 3, 4, 5, 6]))
