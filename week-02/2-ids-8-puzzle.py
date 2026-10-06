GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
INITIAL = (1, 2, 3, 0, 4, 6, 7, 5, 8)

MOVES = {"Up": -3, "Down": 3, "Left": -1, "Right": 1}


def get_neighbors(state):
    """Return list of (move_name, new_state) reachable from state."""
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


def depth_limited_search(state, path, visited, limit):
    """DFS restricted to a given depth. Returns the path to GOAL or None."""
    if state == GOAL:
        return path

    if len(path) >= limit:
        return None

    for move, next_state in get_neighbors(state):
        if next_state in visited:
            continue

        visited.add(next_state)
        result = depth_limited_search(
            next_state, path + [(move, next_state)], visited, limit
        )
        if result is not None:
            return result
        visited.remove(next_state)

    return None


def iterative_deepening_search(state, max_depth=20):
    """Call depth_limited_search for depth = 0, 1, 2, ... until solved."""
    for limit in range(max_depth + 1):
        print(f"Trying depth limit: {limit}")
        result = depth_limited_search(state, [], {state}, limit)
        if result is not None:
            return result
    return None


def print_state(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


def main():
    print("Initial State:")
    print_state(INITIAL)
    print("Goal State:")
    print_state(GOAL)

    result = iterative_deepening_search(INITIAL)

    if result is None:
        print("No solution found within max depth.")
        return

    print(f"\nSolution found in {len(result)} moves:\n")
    for move, state in result:
        print(f"Move: {move}")
        print_state(state)


if __name__ == "__main__":
    main()
