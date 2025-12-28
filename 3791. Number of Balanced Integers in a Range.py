# https://leetcode.com/problems/number-of-balanced-integers-in-a-range/description/
# standard digit DP
# Since n is only up to 10^15 there are barely any states

def countBalanced(low: int, high: int) -> int:
    def solve_lower(n):
        s = list(map(int, str(n)))
        le = len(s)

        mx_s = 2 * ((le + 1) // 2 * 9 + 2)
        dp = [[[-1] * mx_s for _ in range(le + 1)] for _ in range(2)]

        # dp[upper][idx][sum difference] ~2000 states

        def solve(upper, idx, total):
            if idx == le:
                return total == 0
            if dp[upper][idx][total] != -1:
                return dp[upper][idx][total]
            mx_digit = s[idx] if upper else 9
            res = 0
            for digit in range(mx_digit + 1):
                delta = -digit if idx % 2 == 0 else digit
                res += solve(upper and (digit == s[idx]),
                             idx + 1,
                             total + delta)
            dp[upper][idx][total] = res
            return res

        return solve(True, 0, 0)

    return solve_lower(high) - solve_lower(low - 1)
