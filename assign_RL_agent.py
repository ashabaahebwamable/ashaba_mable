#ASSIGNMENT: One train RL agent to navigate to cross the road with action right, left, right
import numpy as np
import random

# Define environment
positions = 5            # Number of positions on the road (0 to 4)
actions = 3              # 0 = left, 1 = stay, 2 = right

# Initialize Q-table [states x actions]
Q = np.zeros((positions, actions))

# Parameters
episodes = 1000
learning_rate = 0.8
gamma = 0.9
epsilon = 0.3

# Training loop
for episode in range(episodes):
    state = 0  # Start at position 0 (start of the road)
    done = False

    while not done:
        # Epsilon-greedy action selection
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, actions - 1)  # Explore
        else:
            action = np.argmax(Q[state])             # Exploit

        # Transition to next state
        if action == 0:  # left
            next_state = max(0, state - 1)
        elif action == 1:  # stay
            next_state = state
        else:  # right
            next_state = min(positions - 1, state + 1)

        # Reward
        reward = 1 if next_state == positions - 1 else 0

        # Q-learning update
        Q[state, action] = Q[state, action] + learning_rate * (
            reward + gamma * np.max(Q[next_state]) - Q[state, action]
        )

        state = next_state

        if state == positions - 1:
            done = True

# Print learned Q-table
print("Trained Q-table:")
print(Q)

# Test the trained agent
print("\nTesting Agent Path:")
state = 0
steps = 0
path = [state]

while state != positions - 1 and steps < 20:
    action = np.argmax(Q[state])
    if action == 0:
        next_state = max(0, state - 1)
    elif action == 1:
        next_state = state
    else:
        next_state = min(positions - 1, state + 1)
    
    state = next_state
    path.append(state)
    steps += 1

print("Agent crossed the road with path:", path)
