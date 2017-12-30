import random as ran

def swap(tour1):

    n = len(tour1)
    I = ran.sample(range(0,n),2)

    i1 = I[0]
    i2 = I[1]

    tour2 = tour1
    tour2 [i2] = tour1[i1]
    tour2 [i1] = tour1[i2]


    return ({"tour2":tour2,"i1":i1,"i2":i2})

