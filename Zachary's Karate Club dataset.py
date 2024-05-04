import networkx as nx
import matplotlib.pyplot as plt

# Load Zachary's Karate Club dataset
G = nx.karate_club_graph()

# Compute degree centrality
degree_centrality = nx.degree_centrality(G)

# Compute betweenness centrality
betweenness_centrality = nx.betweenness_centrality(G)

# Compute closeness centrality
closeness_centrality = nx.closeness_centrality(G)

# Print results
print("Degree Centrality:")
for node, centrality in degree_centrality.items():
    print(f"Node {node}: {centrality}")

print("\nBetweenness Centrality:")
for node, centrality in betweenness_centrality.items():
    print(f"Node {node}: {centrality}")

print("\nCloseness Centrality:")
for node, centrality in closeness_centrality.items():
    print(f"Node {node}: {centrality}")

# Draw the graph
pos = nx.spring_layout(G)  # Layout for the graph
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500)
plt.title("Zachary's Karate Club Network")
plt.show()
