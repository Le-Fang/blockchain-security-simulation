import pickle
from blockchainEnv import BlockchainEnv
import numpy as np
from qlearning import discretize

with open('q_table.pkl', 'rb') as f:
    q_table = pickle.load(f)

# Test the trained agent
num_blocks_until_win = []
for i in range(500):
    env = BlockchainEnv()
    state = env.reset()
    state = discretize(state)
    done = False
    #env.render()
    rewards = []
    while not done:
        action = np.argmax(q_table[state])
        next_state, reward, done, _ = env.step(action)
        rewards.append(reward)
        next_state = discretize(next_state)
        state = next_state
        env.render()
    env.close()
    num_blocks_until_win.append(len(rewards))

print("Average number of blocks until win:", np.mean(num_blocks_until_win))

