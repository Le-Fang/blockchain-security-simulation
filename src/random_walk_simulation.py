import numpy as np

def random_walk(initial_state):
    colors = ['a', 'h']
    probabilities = [0.3, 0.7]
    curent_state = initial_state
    step = 0
    while (curent_state != -5):
        color = np.random.choice(colors, p=probabilities)
        if color == 'a':
            curent_state -= 1
        else:
            curent_state += 1
        step += 1
        if step > 10000:
            break
    return step

def calculate_average_steps(initial_state):
    steps = []
    for i in range(1000):
        steps.append(random_walk(initial_state))
    return np.mean(steps)

print("S_0: Average number of steps until the first violation occurs:", calculate_average_steps(0))
print("S_1: Average number of steps until the first violation occurs:", calculate_average_steps(1))

    