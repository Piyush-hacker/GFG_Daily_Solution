class Solution:
    def maxEdgesToAdd(self, V, edges):
        E = len(edges)
        max_total_edges = (V * (V - 1)) // 2
        additional_edges = max_total_edges - E
        return additional_edges