from __future__ import annotations
import networkx as nx
import pandas as pd

def build_route_digraph(routes_clean: pd.DataFrame) -> nx.DiGraph:
    """
    Build a directed graph where nodes are airport_ids and edges are routes.
    Baseline: one edge per route row (duplicates allowed; NetworkX will merge identical edges).
    """
    G = nx.DiGraph()
    edges = list(zip(routes_clean["src_airport_id"], routes_clean["dst_airport_id"]))
    G.add_edges_from(edges)
    return G