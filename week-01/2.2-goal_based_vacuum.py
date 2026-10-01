state = {"A": "Dirty", "B": "Dirty"}
location = "A"
model = {"A": "Unknown", "B": "Unknown"}


def goal_based_agent(model):
    if model["A"] == "Clean" and model["B"] == "Clean":
        return "NoOp"
    if model[location] == "Dirty":
        return "Suck"
    return "MoveRight" if location == "A" else "MoveLeft"


print("Start:", state, "| location:", location)

for _ in range(5):
    model[location] = state[location]
    action = goal_based_agent(model)

    if action == "Suck":
        state[location] = "Clean"
        model[location] = "Clean"
    elif action == "MoveRight":
        location = "B"
    elif action == "MoveLeft":
        location = "A"

    print(f"Action: {action} | State: {state} | Model: {model}")

    if action == "NoOp":
        print("Goal achieved: both locations are Clean.")
        break