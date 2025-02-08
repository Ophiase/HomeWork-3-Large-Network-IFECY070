from typing import List
import networkx as nx
import random
import matplotlib.pyplot as plt

class GraphGeneration:
    @staticmethod
    def erdos_graph_p(n_vertices, probability=None) -> nx.Graph:
        if probability is None:
            probability = 0.5

        g = nx.Graph()
        g.add_nodes_from(range(n_vertices))

        for i in range(n_vertices):
            for j in range(i + 1, n_vertices):
                if random.random() < probability:
                    g.add_edge(i, j)

        return g

    @staticmethod
    def erdos_graph_m(n_vertices, m_edges) -> nx.Graph:
        if m_edges is None:
            m_edges = n_vertices // 2

        g = nx.Graph()
        g.add_nodes_from(range(n_vertices))

        edges_added = 0
        while edges_added < m_edges:
            u = random.randint(0, n_vertices - 1)
            v = random.randint(0, n_vertices - 1)
            if u != v and not g.has_edge(u, v):
                g.add_edge(u, v)
                edges_added += 1

        return g

    @staticmethod
    def _partition_nodes(n: int, n_partitions: int = 4) -> List[List[int]]:
        groups = []
        base = n // n_partitions
        remainder = n % n_partitions
        start = 0
        for i in range(n_partitions):
            group_size = base + (1 if i < remainder else 0)
            groups.append(list(range(start, start + group_size)))
            start += group_size

        return groups

    @staticmethod
    def tp3_graph(n: int, p: float, q: float, n_partitions: int = 4) -> nx.Graph:
        g = nx.Graph()
        g.add_nodes_from(range(n))
        groups = GraphGeneration._partition_nodes(n, n_partitions=n_partitions)
        for group in groups:
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    if random.random() < p:
                        g.add_edge(group[i], group[j])
        for i in range(len(groups)):
            for j in range(i + 1, len(groups)):
                for u in groups[i]:
                    for v in groups[j]:
                        if random.random() < q:
                            g.add_edge(u, v)
        return g

###################################################################################


def display_graph(g: nx.Graph, title: str) -> None:
    plt.figure()
    nx.draw(g, with_labels=True)
    plt.title(title)
    plt.show()


def main() -> None:
    graph_params = [
        ("Erdos-Renyi p", GraphGeneration.erdos_graph_p, (10, 0.3)),
        ("Erdos-Renyi m", GraphGeneration.erdos_graph_m, (10, 15)),
        ("TP3 Graph", GraphGeneration.tp3_graph, (16, 0.8, 0.2)),
        ("TP3 Graph", GraphGeneration.tp3_graph, (50, 0.95, 0.02))
    ]

    plt.figure(figsize=(15, 5))
    for i, (title, graph_func, params) in enumerate(graph_params, 1):
        g = graph_func(*params)
        plt.subplot(1, 4, i)
        nx.draw(g, with_labels=True)
        plt.title(title)
    plt.show()


if __name__ == "__main__":
    main()
