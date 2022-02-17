import matplotlib.pyplot as plt
import pandas as pd
import itertools


def calc_dice_probibilty_hit(advantage=False, disadvantage=False):
    d = get_dice_range(20)
    if (advantage or disadvantage) and not (advantage and disadvantage):
        tot = [(i,j) for j in d for i in d]
        if advantage: d = [max(i) for i in tot]
        elif disadvantage: d = [min(i) for i in tot]
    pd.DataFrame(d)[0].value_counts().plot()

def cal_dmg(d4=0, d6=0, d8=0, d10=0, d12=0, base=0):
    total = []
    for i in range(d4):
        total.append(get_dice_range(4))
    for i in range(d6):
        total.append(get_dice_range(6))
    for i in range(d8):
        total.append(get_dice_range(8))
    for i in range(d10):
        total.append(get_dice_range(10))
    for i in range(d12):
        total.append(get_dice_range(12))

    total.append([base])

    dmg = list(itertools.product(*total))
    df = pd.DataFrame([sum(i) for i in dmg])
    df = pd.DataFrame(df.value_counts().sort_index())
    total_sum = sum(df.values)
    df.columns = ['prob']
    df['prob'] = df['prob'] / total_sum
    df.index = df.index.map(lambda x: x[0])
    df.plot()
    return sum(df.reset_index()['index'].values * df['prob'].values)




def get_dice_range(d):
    return [i for i in range(1, d+1)]