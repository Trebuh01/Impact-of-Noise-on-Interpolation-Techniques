import pandas as pd
import matplotlib.pyplot as plt

node_counts = [4, 7, 15, 20]
noise_level = 0.5
def nodes_select(data, count):
    indices = []
    for i in range(count):
        quantile = i / (count - 1)
        index = int(round(pd.Series(range(len(data))).quantile(quantile)))
        indices.append(index)

    x_nodes = data.loc[indices, 'Dystans'].tolist()
    y_nodes = data.loc[indices, 'Wysokość'].tolist()

    return x_nodes, y_nodes

def add_noise(y_values, noise_level):
    noisy_y_values = y_values.copy()
    for i in range(1, len(y_values) - 1):
        noise = noise_level * (y_values[i+1] - y_values[i-1]) / 2
        noisy_y_values[i] += noise
    return noisy_y_values


def plot_results(x, y, x_nodes, y_nodes, x_interp, y_interp, method, filename):
    plt.figure(figsize=(12, 8))
    plt.scatter(x, y, color='blue', label='Dane oryginalne', s=10, alpha=0.6)
    plt.scatter(x_nodes, y_nodes, color='red', label='Węzły interpolacji', s=50, edgecolor='black')
    plt.plot(x_interp, y_interp, color='green', linestyle='--', linewidth=2, label=method)
    plt.grid(True, linestyle='-.', linewidth=0.7)
    plt.xlabel('Dystans (m)', fontsize=14)
    plt.ylabel('Wysokość (m)', fontsize=14)
    plt.title(f'{method} z {len(x_nodes)} węzłami', fontsize=16, fontweight='bold')
    plt.legend(loc='best', fontsize=12)
    plt.savefig(filename, bbox_inches='tight')
    plt.close()
