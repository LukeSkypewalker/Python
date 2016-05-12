import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

graph = [('A', 'B', 3), ('B', 'C', 4), ('C', 'A', 5)]


G.add_weighted_edges_from(graph)
pos=nx.shell_layout(G)

# nx.draw_spring(G)

# G.pos[i]=(float(x),float(y))

nx.draw_networkx_nodes(G,pos,node_size=300)
nx.draw_networkx_edges(G,pos, width=3)
nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')

plt.show()
