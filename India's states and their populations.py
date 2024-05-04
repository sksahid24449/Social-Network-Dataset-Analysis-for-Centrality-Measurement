import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Define India's states and their populations (in millions)
state_population = {
    'Andhra Pradesh': 539,
    'Arunachal Pradesh': 17,
    'Assam': 312,
    'Bihar': 104,
    'Chhattisgarh': 29,
    'Goa': 15,
    'Gujarat': 636,
    'Haryana': 292,
    'Himachal Pradesh': 68,
    'Jharkhand': 36,
    'Karnataka': 675,
    'Kerala': 356,
    'Madhya Pradesh': 853,
    'Maharashtra': 1237,
    'Manipur': 30,
    'Meghalaya': 32,
    'Mizoram': 12,
    'Nagaland': 22,
    'Odisha': 462,
    'Punjab': 298,
    'Rajasthan': 772,
    'Sikkim': 7,
    'Tamil Nadu': 756,
    'Telangana': 391,
    'Tripura': 36,
    'Uttar Pradesh': 237,
    'Uttarakhand': 11,
    'West Bengal': 991,
    'Delhi': 302,  # Including Delhi as a state for simplicity
    'Jammu and Kashmir': 136,  # Including Jammu and Kashmir as a state for simplicity
    'Ladakh': 0.293,  # Including Ladakh as a state for simplicity
    'Puducherry': 1.247  # Including Puducherry as a state for simplicity
}

# Add nodes (India's states) with population as an attribute
for state, population in state_population.items():
    G.add_node(state, population=population)

# Define edges (you can define edges based on proximity, economic ties, etc.)
# For simplicity, let's assume edges between neighboring states
state_neighbors = {
    'Andhra Pradesh': ['Telangana', 'Odisha', 'Karnataka', 'Tamil Nadu'],
    'Arunachal Pradesh': ['Assam'],
    'Assam': ['Arunachal Pradesh', 'Nagaland', 'Manipur', 'Mizoram', 'Meghalaya'],
    'Bihar': ['Uttar Pradesh', 'Jharkhand', 'West Bengal'],
    'Chhattisgarh': ['Odisha', 'Jharkhand', 'Madhya Pradesh', 'Maharashtra', 'Telangana'],
    'Goa': ['Karnataka', 'Maharashtra'],
    'Gujarat': ['Rajasthan', 'Madhya Pradesh', 'Maharashtra'],
    'Haryana': ['Punjab', 'Himachal Pradesh', 'Uttar Pradesh', 'Rajasthan'],
    'Himachal Pradesh': ['Jammu and Kashmir', 'Punjab', 'Haryana', 'Uttarakhand'],
    'Jharkhand': ['Bihar', 'West Bengal', 'Odisha', 'Chhattisgarh', 'Uttar Pradesh'],
    'Karnataka': ['Maharashtra', 'Goa', 'Kerala', 'Tamil Nadu', 'Telangana', 'Andhra Pradesh'],
    'Kerala': ['Karnataka', 'Tamil Nadu'],
    'Madhya Pradesh': ['Rajasthan', 'Uttar Pradesh', 'Chhattisgarh', 'Maharashtra', 'Gujarat'],
    'Maharashtra': ['Gujarat', 'Madhya Pradesh', 'Chhattisgarh', 'Telangana', 'Karnataka', 'Goa'],
    'Manipur': ['Mizoram', 'Assam', 'Nagaland'],
    'Meghalaya': ['Assam'],
    'Mizoram': ['Assam', 'Manipur'],
    'Nagaland': ['Assam', 'Manipur', 'Arunachal Pradesh'],
    'Odisha': ['Chhattisgarh', 'Jharkhand', 'West Bengal', 'Andhra Pradesh', 'Telangana'],
    'Punjab': ['Haryana', 'Himachal Pradesh'],
    'Rajasthan': ['Gujarat', 'Madhya Pradesh', 'Uttar Pradesh', 'Haryana'],
    'Sikkim': ['West Bengal'],
    'Tamil Nadu': ['Karnataka', 'Kerala', 'Andhra Pradesh'],
    'Telangana': ['Andhra Pradesh', 'Maharashtra', 'Chhattisgarh', 'Karnataka', 'Odisha'],
    'Tripura': ['Assam'],
    'Uttar Pradesh': ['Haryana', 'Rajasthan', 'Madhya Pradesh', 'Bihar', 'Jharkhand', 'Uttarakhand', 'Himachal Pradesh', 'Delhi'],
    'Uttarakhand': ['Uttar Pradesh', 'Himachal Pradesh', 'Haryana'],
    'West Bengal': ['Jharkhand', 'Bihar', 'Sikkim', 'Odisha', 'Jharkhand'],
    'Delhi': ['Uttar Pradesh', 'Haryana', 'Punjab', 'Rajasthan', 'Uttarakhand'],
    'Jammu and Kashmir': ['Himachal Pradesh', 'Punjab'],
    'Ladakh': ['Himachal Pradesh', 'Jammu and Kashmir'],
    'Puducherry': ['Tamil Nadu']
}

# Add edges (neighbor relationships)
for state, neighbors in state_neighbors.items():
    for neighbor in neighbors:
        G.add_edge(state, neighbor)

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

# Draw the graph (with node sizes proportional to population)
node_size = [pop * 20 for pop in nx.get_node_attributes(G, 'population').values()]  # Scale
# Draw the graph
pos = nx.spring_layout(G)  # Layout for the graph
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, arrowsize=10)
plt.title("Cricket Social Network")
plt.show()
