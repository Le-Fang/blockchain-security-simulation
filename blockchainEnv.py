import gym
from gym import spaces
import numpy as np

class BlockchainEnv(gym.Env):
    def __init__(self):
        super(BlockchainEnv, self).__init__()
        
        # Action space: 0 = mine privately, 1 = reset private chain to the public chain height
        self.action_space = spaces.Discrete(2)
        
        # Observation space: [height of public chain, height of private chain]
        self.observation_space = spaces.Box(low=0, high=np.inf, shape=(2,), dtype=np.float32)
        
        # Initial state
        self.reset()
        
    def reset(self):
        # Public chain height
        self.public_chain_height = 0
        
        # Private chain height
        self.private_chain_height = 0
        
        # Return initial observation
        return np.array([self.public_chain_height, self.private_chain_height])
        
    def step(self, action):
        assert self.action_space.contains(action), f"{action} invalid"
        
        if action == 0:
            # Adversary mines privately
            if np.random.binomial(1, 0.3) == 1:
                # Adversary mines a block on the private chain
                self.private_chain_height += 1
            else:
                self.public_chain_height += 1
        elif action == 1:
            # Adversary resets the private chain to the public chain height
            reward = -self.private_chain_height - self.public_chain_height - 1
            self.private_chain_height = 0
            self.public_chain_height = 0
            if np.random.binomial(1, 0.3) == 1:
                self.private_chain_height += 1
            else:
                self.public_chain_height += 1
            done = False
            observation = np.array([self.public_chain_height, self.private_chain_height])
            return observation, reward, done, {}
        
        
        # Calculate reward
        reward = -1

        if self.public_chain_height >= 5 and self.private_chain_height >= self.public_chain_height:
            reward = 9999999  # Adversary wins
            done = True
        else:
            if self.private_chain_height - self.public_chain_height >= 5:
                #edge case: the adversary wins already (want to wait until the target block is actually confirmed)
                reward = 0
            done = False
        
        # Create observation
        observation = np.array([self.public_chain_height, self.private_chain_height])
        
        return observation, reward, done, {}
    
    def render(self, mode='human'):
        print(f"Public chain height: {self.public_chain_height}, Private chain height: {self.private_chain_height}")
    
    def close(self):
        pass
