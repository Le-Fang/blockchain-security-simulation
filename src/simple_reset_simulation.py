import numpy as np

rate = 1
colors = ['a', 'h']
probabilities = [0.3, 0.7]

inter_arrival_times = np.random.exponential(scale=1/rate, size=5000)

arrival_times = np.cumsum(inter_arrival_times)

num_blocks_until_win = []
for i in range(1000):
    length_of_public_chain = 0
    length_of_private_chain = 0

    for i, arrival_time in enumerate(arrival_times):
        #mine a block
        color = np.random.choice(colors, p=probabilities)
        if color == 'a':
            length_of_private_chain += 1
        else:
            length_of_public_chain += 1

        #check if the adversary wins
        if length_of_public_chain >= 5 and length_of_private_chain >= length_of_public_chain:
            num_blocks_until_win.append(i+1)
            break

        #silly adversary strategy: reset if the public chain is longer
        if length_of_private_chain < length_of_public_chain:
            #reset
            length_of_public_chain = 0
            length_of_private_chain = 0

print("Average number of blocks until the first violation occurs:", np.mean(num_blocks_until_win))