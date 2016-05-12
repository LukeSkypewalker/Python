import networkx as nx
import matplotlib.pyplot as plt
n = 10
G = nx.navigable_small_world_graph(n, p=1, q=1, r=2, dim=2, seed=None)
nx.draw_spring(G)
plt.show()

