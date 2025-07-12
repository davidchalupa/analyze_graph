import argparse
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

from analyze_graph.loader import load_from_col_file
from analyze_graph.dominating_set import minimum_dominating_set_ilp


def visualize_dominating_set(G, mds):
    labels = [0] * G.number_of_nodes()
    for node in mds:
        labels[node] = 1
    print(labels)
    pos = nx.spring_layout(G, iterations=100)
    # pos = nx.spiral_layout(G)

    nx.draw_networkx_nodes(G, pos, node_size=50, node_color=labels, cmap=plt.cm.rainbow)
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    plt.title('Minimum dominating set of a graph')
    plt.axis('off')
    plt.show()


def minimum_dominating_set(G):
    print("Computing minimum dominating set of the graph...")

    mds = minimum_dominating_set_ilp(G, timeLimit=120)

    if mds is not None:
        print(f"Found a dominating set of size {len(mds)}.")
    else:
        print(f"No feasible solution found.")

    visualize_dominating_set(G, mds)


def load_graph(file_name):
    print("Loading the graph from file...")

    G = load_from_col_file(file_name)
    print(f"Graph has {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")
    return G


def parse_args():
    parser = argparse.ArgumentParser(
        description="A tool for analysis of graphs."
    )

    parser.add_argument(
        "--minimum-dominating-set",
        action="store_true",
        help="Compute minimum dominating set of the graph."
    )

    parser.add_argument(
        "file",
        type=str,
        help="Path to the file to process"
    )

    # Parse the arguments
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    print(args.file)
    G = load_graph(Path(args.file))

    if args.minimum_dominating_set:
        minimum_dominating_set(G)
