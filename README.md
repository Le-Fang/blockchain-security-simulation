This repository contains 1. reinforcement learning algorithm for private mining with resets attack on a blockchain system, and 2. a simulation that evaluates a simple reset policy.

Files:

blockchainEnv.py: this is a env class that inherits gym.Env; this custom enviroment simulates a blockchain system, in which the adversary tries to create a safety violation by private mining with resets attack. For simplicity, propagation delay is assumed to be 0 (all honest nodes have the same view on the longest honest chain). In this env, the adversary mining power a is set to be 0.3, and the honest mining power h is set to be 0.7; the confirmation number k is set to be 5.

qlearning.py: this is the qlearning algorithm that trains an agent to learn an adversary policy. Hyperparamters are defined inside. 

testing_qlearner.py: this is a file to evaluate the learned policy. It reads from q_table.pkl and simulates the performce of the policy.

simple_reset_simulation.py: this file contains a simulation of a simple reset policy (reset whenever the public chain is longer than the private chain).

How to use:

By running simple_reset_simulation.py, it simply prints out the average number of blocks mined before the first violation occurs.

By running testing_qlearner.py, it reads the learned policy from q_table.pkl, and tests its performance.

You can also re-train a new policy by running qlearning.py(maybe change some hyperparameters); currently, it stores the new policy in q_table_temp.pkl; if you want to test your new policy, you can update the testing_qlearner.py such that it reads the policy from q_table_temp.pkl.