import numpy as np

MAX_NUM = 37

def draw_to_multihot(draw):
    v = np.zeros(MAX_NUM)
    for n in draw:
        v[n-1] = 1
    return v

def make_features(prev_draws):
    W = len(prev_draws)
    mats = np.array([draw_to_multihot(d) for d in prev_draws])

    counts = mats.sum(axis=0)

    recency = np.full(MAX_NUM, W+1)
    for i in range(W):
        idx = np.where(mats[W-1-i] == 1)[0]
        recency[idx] = np.minimum(recency[idx], i)

    momentum = mats[-3:].sum(axis=0) - mats[:-3].sum(axis=0)

    return np.concatenate([counts, recency, momentum])
