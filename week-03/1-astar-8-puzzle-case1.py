"""8-Puzzle using A* search.  Case 1: f(n) = g(n) + h(n)
g(n) = depth of the node, h(n) = number of misplaced tiles."""

import heapq

INITIAL = (2, 8, 3, 1, 6, 4, 7, 0, 5)
GOAL = (1, 2, 3, 8, 0, 4, 7, 6, 5)

MOVES = {"Up": -3, "Down": 3, "Left": -1, "Right": 1}


def get_neighbors(state):
    blank = state.index(0)
    row, col = divmod(blank, 3)
    neighbors = []

    for move, delta in MOVES.items():
        if move == "Up" and row == 0:
            continue
        if move == "Down" and row == 2:
            continue
        if move == "Left" and col == 0:
            continue
        if move == "Right" and col == 2:
            continue

        new_blank = blank + delta
        new_state = list(state)
        new_state[blank], new_state[new_blank] = new_state[new_blank], new_state[blank]
        neighbors.append((move, tuple(new_state)))

    return neighbors


def heuristic(state):
    """h(n): number of tiles not in their goal position (blank not counted)."""
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != GOAL[i])


def print_state(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


g_cost = {INITIAL: 0}
counter = 0
frontier = [(heuristic(INITIAL), counter, INITIAL, [])]

print("Initial State:")
print_state(INITIAL)
print("Goal State:")
print_state(GOAL)

while frontier:
    f, _, state, path = heapq.heappop(frontier)

    if state == GOAL:
        print(f"Solution found in {len(path)} moves:\n")
        for move, s in path:
            g = g_cost[s]
            print(f"Move: {move}  (g={g}, h={heuristic(s)}, f={g + heuristic(s)})")
            print_state(s)
        break

    for move, next_state in get_neighbors(state):
        new_g = g_cost[state] + 1
        if next_state not in g_cost or new_g < g_cost[next_state]:
            g_cost[next_state] = new_g
            counter += 1
            f_new = new_g + heuristic(next_state)
            heapq.heappush(
                frontier, (f_new, counter, next_state, path + [(move, next_state)])
            )
