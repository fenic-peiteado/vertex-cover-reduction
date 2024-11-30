import networkx as nx
import matplotlib.pyplot as plt

def PrintGraph(transform_output):
    G = nx.Graph()
    truth_settings = transform_output["truth-settings"]
    satisfaction_testing = transform_output["satisfaction-testing"]
    communication_edges = transform_output["communication-edges"]
    vertex_output = []
    edge_output = []
    color_map = []

    truth_settings_color = "red"
    satisfaction_testing_color = "blue"
    for vertices in truth_settings["vertices"]:
        vertex_output.append(vertices)
        color_map.append(truth_settings_color)

    for vertices in satisfaction_testing["vertices"]:
        vertex_output.append(vertices)
        color_map.append(satisfaction_testing_color)
    for edge in truth_settings["aristas"]:
        edge_output.append((edge[0], edge[1]))
    for edge in satisfaction_testing["aristas"]:
        edge_output.append((edge[0], edge[1]))       
    for edge in communication_edges["aristas"]:
        edge_output.append((edge[0], edge[1]))
    G.add_nodes_from(vertex_output)        
    G.add_edges_from(edge_output)

    nx.draw(G, node_color = color_map, with_labels = True, font_weight = 'bold')  # networkx draw()
    plt.show()  # pyplot draw()
    