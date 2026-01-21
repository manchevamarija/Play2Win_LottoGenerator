import matplotlib.pyplot as plt

def plot_probs(probs):
    plt.figure(figsize=(12, 4))
    plt.bar(range(1, 38), probs)
    plt.axhline(0.5, linestyle="--")
    plt.xlabel("Број")
    plt.ylabel("Веројатност на појава")
    plt.title("Лото предвидување 1-37")
    plt.tight_layout()
    plt.show()
