import numpy as np

def findMissing(x,y):
    n1 = len(x)
    n2 = len(y)

    if n1 >= n2:
        vec1 = x
        vec2 = y
    else:
        vec1 = y
        vec2 = x

    n1 = len(vec1)
    n2 = len(vec2)

    matchVec = []
    val= float('nan')

    for j in range(n1):
        val1 = vec1[j]
        for k in range(n2):
            val2 = vec2[k]

            if val1 == val2:
                matched = 1
                # print(val1, val2)
            else:
                matched = 0
            matchVec = np.concatenate([matchVec, [matched]])

        if sum(matchVec) == 0:
            val = val1

            break
        matchVec = []

    return val

# -----------------------------

x = [1,2,3,4,5,6,7]
y = x
misMatch =  findMissing(x,y)

if misMatch == misMatch:
    print("Did not find match for %f" % (misMatch))
else:
    print("All values matched")