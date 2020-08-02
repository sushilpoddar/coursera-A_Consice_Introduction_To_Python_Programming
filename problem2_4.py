# %%
import random


def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    lis = []
    random.seed(70)
    for i in range(0,10):
        lis.append(random.random()*5+30)
    print(lis)

# %%