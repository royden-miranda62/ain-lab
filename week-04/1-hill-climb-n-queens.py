"""
State     : x[i] = row of the queen in column i (one queen per column)
Neighbour : swap the row positions of two queens (columns i and j)
Cost      : number of pairs of queens attacking each other
Ties      : pick the neighbour whose swapped pair has the smallest column numbers
"""

N = 4
state = [3, 1, 2, 0]  # initial state from the lab sheet (x0=3, x1=1, x2=2, x3=0)


def cost(x):
    """Number of attacking pairs (same row or same diagonal)."""
    count = 0
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i] == x[j] or abs(x[i] - x[j]) == j - i:
                count += 1
    return count


def print_board(x):
    for row in range(len(x)):
        print(" ".join("Q" if x[col] == row else "." for col in range(len(x))))
    print()


step = 0
current_cost = cost(state)

print("Initial state:", state, "| cost =", current_cost)
print_board(state)

while current_cost > 0:
    step += 1
    print(f"--- Step {step}: current = {state}, cost = {current_cost} ---")

    best_cost = current_cost
    best_state = None
    best_swap = None

    # try every swap (i, j) in order of smallest column numbers first
    for i in range(N):
        for j in range(i + 1, N):
            neighbor = state[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            c = cost(neighbor)
            print(f"  swap (x{i}, x{j}) -> {neighbor}, cost = {c}")

            if c < best_cost:  # strictly better, so earlier swaps win ties
                best_cost = c
                best_state = neighbor
                best_swap = (i, j)

    if best_state is None:
        print("\nNo neighbour has a lower cost. Stuck at a local optimum.")
        break

    print(
        f"  => choose swap (x{best_swap[0]}, x{best_swap[1]}), new cost = {best_cost}\n"
    )
    state = best_state
    current_cost = best_cost

print("\nFinal state:", state, "| cost =", current_cost)
print_board(state)

if current_cost == 0:
    print("Goal reached: no pair of queens is attacking each other.")
