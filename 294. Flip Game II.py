# O(2^n * n), O(n) for converting list to tuple on each function call, 2^n possible states in total

# brute force using memoization: go through all moves until you reach a move
# where you can force your opponent to get stuck (therefore you win)

def canWin(currentState: str) -> bool:
    def win(state):
        hashable = tuple(state)  # try to reuse value
        if hashable in cache:
            return cache[hashable]

        moves = [state[i] == "+" and state[i + 1] == "+" for i in range(n - 1)]  # look for 2 consecutive '+'
        if not any(moves):  # no moves available, lose
            return False

        win_game = False
        for i, move in enumerate(moves):
            if move:  # go through all available moves
                new_state = state.copy()  # create the new state
                new_state[i] = "-"
                new_state[i+1] = "-"

                # since the next turn is your opponent's, if you can make them stuck using any move, you win
                if not win(new_state):
                    win_game = True
                    break

        cache[hashable] = win_game  # store value for later use
        return win_game

    n = len(currentState)
    cache = {}  # memoization
    return win(list(currentState))  # convert to list for easier edits


print(canWin("+++++"))
