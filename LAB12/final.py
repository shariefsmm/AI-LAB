import matplotlib.pyplot as plt
import numpy as np

K = np.random.randint(5,7)  # number of bandit arms
T = 10000                   # number of steps to simulate
print("\nK =", K, "\tT =", T)
mean = (np.sort(np.random.random(K)))[::-1]     # mean of reward distributions of each bandit arm
delta = mean[0] - mean                          # corresponding delta (maximum mean - arm mean)
p = np.zeros((K, T + 1))                        # p[i][j] stores the reward from arm i at time step j
for i in range(K):
    p[i] = np.random.binomial(1, mean[i], T + 1)

S = np.array([p[i][1] for i in range(K)])       # S[i] stores sample mean of rewards from arm i till now
N = np.ones((K, T + 1), dtype=np.int32)         # N[i][j] stores the number of times arm i has been chosen at instant j
t = [0] + [np.log10(i) for i in range(1, T + 1)]    # x-coordinates for plotting the graph

# UCB algorithm
for i in range(2, T + 1):
    UCB = np.array([(S[j] / N[j][i - 1] + np.sqrt(2 * t[i] / N[j][i - 1])) for j in range(K)])
    ind = np.argmax(UCB)
    S[ind] += p[ind][i]
    for j in range(K):
        N[j][i] = N[j][i - 1]
    N[ind][i] += 1

print("\nDeltas are as follows:")
for i in range(K):
    print("%.2f" % delta[i], end="\t")

delta_slope = [0] + [(1 / k)**2 for k in delta[1:]]
print("\n\nSlope from deltas:")
for i in range(K):
    print("%.2f" % delta_slope[i], end="\t")

print("\n\nSlope from graph:")
graph_slope = [0] + [(N[i][T] - N[i][0]) / t[T] for i in range(1, K)]
for i in range(K):
    print("%.2f" % graph_slope[i], end="\t")

print()
# plotting the graph
for i in range(K):
    plt.plot(t[1:], N[i][1:])
plt.show()
