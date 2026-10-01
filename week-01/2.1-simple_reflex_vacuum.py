import random

state = {
    "A": random.choice(["Clean", "Dirty"]), 
    "B": random.choice(["Clean", "Dirty"])
}
location = "A"


def simple_reflex_agent(location, status):
    if status == "Dirty":
        return "Suck"
    return "MoveRight" if location == "A" else "MoveLeft"


print("Start:", state, "| location:", location)

for _ in range(5):
    status = state[location]
    action = simple_reflex_agent(location, status)
    print(f"Percept: ({location}, {status}) -> Action: {action}", end=" | ")

    if action == "Suck":
        state[location] = "Clean"
    elif action == "MoveRight":
        location = "B"
    elif action == "MoveLeft":
        location = "A"

    print(f"State: {state}")

    if state["A"] == "Clean" and state["B"] == "Clean":
        print("Environment is clean.")
        break
