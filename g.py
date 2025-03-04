import networkx as nx
import matplotlib.pyplot as plt

network = nx.Graph()
network.add_nodes_from([1,2,3,4,5])
print(f"This network has now {network.number_of_nodes()} nodes.")

network.add_edge(1,3)
network.add_edge(1,4)
network.add_edge(3,5)
network.add_edge(2,5)
network.add_edge(2,4)
# network.add_edge(4,5)
# network.add_edge(1,5)
# network.add_edge(3,4)
# Ensuring correct number of colors
color_list = ["gold", "red", "violet", "blue", "green"]

plt.figure(figsize=(8, 6))
plt.title('Example of Graph Representation', size=10) 

nx.draw_networkx(network, node_color=color_list, with_labels=True)
plt.show()
