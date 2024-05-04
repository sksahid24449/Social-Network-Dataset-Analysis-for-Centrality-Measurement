import networkx as nx
import matplotlib.pyplot as plt

# Define a simple cricket social network dataset (player, teammate) relationships
cricket_data = {
    'Sachin Tendulkar': ['Sourav Ganguly', 'Rahul Dravid', 'Virender Sehwag'],
    'Sourav Ganguly': ['Sachin Tendulkar', 'Rahul Dravid'],
    'Rahul Dravid': ['Sachin Tendulkar', 'Sourav Ganguly', 'VVS Laxman'],
    'Virender Sehwag': ['Sachin Tendulkar', 'Gautam Gambhir'],
    'VVS Laxman': ['Rahul Dravid'],
    'Gautam Gambhir': ['Virender Sehwag']
}

# Create a directed graph
G = nx.DiGraph()

# Add nodes (cricket players)
for player in cricket_data.keys():
    G.add_node(player)

# Add edges (teammate relationships)
for player, teammates in cricket_data.items():
    for teammate in teammates:
        G.add_edge(teammate, player)

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
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, arrowsize=10)
plt.title("Cricket Social Network")
plt.show()
