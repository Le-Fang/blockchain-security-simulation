import numpy as np
from blockchainEnv import BlockchainEnv
import pickle

# Discretize the state space
def discretize(state):
    return tuple(np.clip((state // 1).astype(int), 0, 100))

if __name__ == '__main__':
    env = BlockchainEnv()

    # Q-learning parameters
    alpha = 0.4  # Learning rate
    gamma = 0.95  # Discount factor
    epsilon = 0.2  # Exploration rate
    num_episodes = 10000

    # Q-table initialization
    q_table = np.zeros([1001, 1001, env.action_space.n])


    # Training the agent
    for episode in range(num_episodes):
        state = env.reset()
        state = discretize(state)
        done = False
        
        while not done:
            if np.random.uniform(0, 1) < epsilon:
                action = env.action_space.sample()  # Explore action space
            else:
                action = np.argmax(q_table[state])  # Exploit learned values
            
            next_state, reward, done, _ = env.step(action)
            next_state = discretize(next_state)
            
            old_value = q_table[state + (action,)]
            next_max = np.max(q_table[next_state])
            
            # Q-learning formula
            new_value = old_value + alpha * (reward + gamma * next_max - old_value)
            q_table[state + (action,)] = new_value
            
            state = next_state

    env.close()

    # Save the trained agent to q_table_temp.pkl
    with open('src/q_table_temp.pkl', 'wb') as f:
        pickle.dump(q_table, f)

    print("Training complete.")



