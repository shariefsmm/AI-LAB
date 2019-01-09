import numpy as np
from copy import deepcopy

def makearray(arr):
    hash = 0
    for i in range(len(arr)):
        hash = hash * 3 + arr[i]
    return hash

def conv_hash(num, len):
    arr = []
    for i in range(len):
        arr.append(num % 3)
        num = num // 3
    arr.reverse()
    return arr

Pi = np.ones((250, 11, 4), dtype=np.int32) * -1      # Pi[i][j] stores the optimal policy when i overs and j wickets are left
V = np.zeros((250, 11, 4))                           # V[i][j] stores the value when we start following our optimal policy

A = np.array([0, 1, 2, 3, 4], dtype=np.int32)        # our action space

# strike rate and economy array for bowlers
es = np.array([(3, 33), (3.5, 30), (4, 6), (4.5, 6), (5, 15)], dtype=np.float32)

pw = [(6.0 / es[i][1]) for i in range(5)]       # pw[i] stores the probability that bowler i will take a wicket in an over

for i in range(1, 11):
    for j in range(1, 4):
        V[0][i][j] = 0
        Pi[0][i][j] = -1

# performing finite horizon value iteration to find optimal policy and value function
for j in range(1, 11):
    for k in range(1, 4):
        for i in range(1, 243):
            p = conv_hash(i, 5)
            minV = 100000000
            minInd = -1
            for t in range(5):
                if p[t] == 0:
                    continue
                newb = deepcopy(p)
                newb[t] = newb[t] - 1
                tempV = pw[t] * V[makearray(newb)][j - 1][k - 1] + (1 - pw[t]) * V[makearray(newb)][j - 1][k] + es[t][0]
                if tempV < minV:
                    minV = tempV
                    minInd = t
            V[i][j][k] = minV
            Pi[i][j][k] = minInd


print("Optimal Value and Policy:")
print("Overs left Bowlers over","\twicketsleft optimal Value  Ploicy")
for i in range(1, 11):
    for j in range(1, 4):
        for k in range(243):
            # print("Overs left:",i," and", conv_hash(k, 5), "wickets left:",j, end="\t")
            # print("%.2f" % V[k][i][j], " ", Pi[k][i][j])
            print(i,"\t\t"," ",conv_hash(k,5)," ",j,"\t\t\t",V[k][i][j],"\t\t\t",Pi[k][i][j])

# simulate
for k in range(10):
    print("\n\n\t\tGame ",k+1)
    over_left = [2, 2, 2, 2, 2]
    wickets_left = 3
    runs = 0
    for i in range(0, 10):
        print("\n")
        wf = np.random.uniform(1, 2)
        bowler = Pi[makearray(over_left)][10 - i][wickets_left]
        print("Over", i + 1)
        print("Current Overs left of each bowler:", over_left)
        print("Current runs", runs)
        print("Current Wickets Left", wickets_left)
        print("Bowler:", bowler, end="\t")
        print("Runs scored:", es[bowler][0])
        runs += es[bowler][0]
        over_left[bowler] -= 1
        if wf >= pw[bowler]:
            print("Wicket fell")
            wickets_left -= 1
        else:
            print("Wicket didn't fall")
        if wickets_left == 0:
            break