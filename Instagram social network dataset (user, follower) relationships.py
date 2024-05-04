import networkx as nx
import matplotlib.pyplot as plt

# Define a simple Instagram social network dataset (user, follower) relationships
instagram_data = {
   'Alice': ['Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah'],
    'Bob': ['Alice', 'Charlie', 'David', 'Eve'],
    'Charlie': ['Alice', 'Bob', 'David', 'Eve', 'Frank'],
    'David': ['Alice', 'Charlie', 'Eve', 'Frank', 'Grace'],
    'Eve': ['Alice', 'Bob', 'Charlie', 'David', 'Frank', 'Grace', 'Hannah'],
    'Frank': ['Alice', 'Charlie', 'David', 'Eve', 'Grace'],
    'Grace': ['Alice', 'David', 'Eve', 'Frank', 'Hannah'],
    'Hannah': ['Alice', 'Eve', 'Grace']
}


# Create a directed graph
G = nx.DiGraph()

# Add nodes (Instagram users)
for user in instagram_data.keys():
    G.add_node(user)

# Add edges (follower-followee relationships)
for user, followers in instagram_data.items():
    for follower in followers:
        G.add_edge(follower, user)

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
plt.title("Instagram Social Network")
plt.show()
