import pickle
from blockchainEnv import BlockchainEnv
import numpy as np
from qlearning import discretize

# Load the trained agent from q_table.pkl
# you can run qlearning.py to train the agent (it will save the trained agent to q_table_temp.pkl)
with open('src/q_table.pkl', 'rb') as f:
    q_table = pickle.load(f)

# Test the trained agent
num_blocks_until_win = []
# Run 500 times to get an average number of blocks until the first violation occurs
for i in range(1000):
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
        #env.render()
    env.close()

    #in each step, a new block is mined, so the
    #number of blocks until the first violation is len(rewards)
    num_blocks_until_win.append(len(rewards))

print("Average number of blocks until the first violation occurs:", np.mean(num_blocks_until_win))

