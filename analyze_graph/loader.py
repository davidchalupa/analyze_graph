import networkx as nx

def load_from_col_file(file_path):
    """
    Loads an undirected graph from a .col file into a networkx Graph.

    :param file_path: Path to the .col file
    :return: A networkx Graph object
    """
    G = nx.Graph()

    with open(file_path, 'r') as file:
        for line in file:
            # Strip whitespace and skip comments
            line = line.strip()
            if line.startswith('c'):  # Ignore comment lines
                continue
            if line.startswith('p'):  # Read metadata line
                _, _, num_vertices, num_edges = line.split()
                continue
            if line.startswith('e'):  # Read edge lines
                _, u, v = line.split()
                if u != v:
                    G.add_edge(int(u) - 1, int(v) - 1)
                    G.add_edge(int(v) - 1, int(u) - 1)

    return G
