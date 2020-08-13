def pb(num): # as percent
"""generates the fail/num for an exact number"""
    result = 0
    for i in range(1, num + 1):
        if "1" in str(i):
            result += 1
    return result / num
    
def simpleGeneratorFun(num): # what happens without num here? idk
"""generator to make the code run faster"""
    for i in range (1, num + 1):
        if "1" in str(i):
            yield i #yields numbers that include 1

def pb_list(num):
"""function to append to a total list with probabilities 1-num"""
    num += 2
    has_1 = simpleGeneratorFun(num*10) # can i remove this? idk
    q = []
    i = 1
    count = 0
    r = next(has_1)
    while r < num:
        if i < r:
            j = len(q)
            q.append(count/ i)
            i += 1
        else:
            r = next(has_1)
            count += 1
    return q #returns total list

#plotting every probability of an index.
to_plot = pb_list(2500) # indexes 0-2499, pbs 1-2500
import matplotlib.pyplot as plt
import numpy as np

plt.plot(to_plot)
plt.show()
