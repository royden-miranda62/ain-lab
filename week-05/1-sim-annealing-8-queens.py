"""
State    : x[i] = row of the queen in column i (one queen per column)
Neighbour: swap the row positions of two randomly chosen queens
Cost     : number of pairs of queens attacking each other
"""

import math
import random

N = 8


def cost(x):
    """Number of attacking pairs (same row or same diagonal)."""
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if x[i] == x[j] or abs(x[i] - x[j]) == j - i:
                count += 1
    return count


def print_board(x):
    for row in range(N):
        print(" ".join("Q" if x[col] == row else "." for col in range(N)))
    print()


current = random.sample(range(N), N)  # random initial state (each row used once)
current_cost = cost(current)

T = 100.0  # large positive starting temperature
COOLING = 0.995  # T decreases by this factor every iteration
MIN_T = 0.001  # stop when T is (almost) 0

print("Initial state:", current, "| cost =", current_cost)
print_board(current)

step = 0
while T > MIN_T and current_cost > 0:
    step += 1

    # random neighbour: swap the rows of two queens
    i, j = random.sample(range(N), 2)
    next_state = current[:]
    next_state[i], next_state[j] = next_state[j], next_state[i]
    next_cost = cost(next_state)

    delta_e = current_cost - next_cost

    if delta_e > 0:
        accept = True  # better: always move
    else:
        accept = random.random() < math.exp(
            delta_e / T
        )  # worse: move with p = e^(dE/T)

    if accept:
        current, current_cost = next_state, next_cost

    if step % 100 == 0:
        print(f"Step {step:4d} | T = {T:8.4f} | cost = {current_cost}")

    T *= COOLING

print(f"\nStopped after {step} steps (T = {T:.4f})")
print("Final state:", current, "| cost =", current_cost)
print_board(current)

if current_cost == 0:
    print("Goal reached: no pair of queens is attacking each other.")
else:
    print("Did not reach cost 0 this run. Run again (it is randomised).")
