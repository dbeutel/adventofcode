import bisect
import re
from itertools import combinations as com


def dijkstra(nodes, edges, current):
    dists = {current: 0}
    unvisited = [current] + list(set(nodes) - {current})
    while unvisited:
        current = unvisited.pop(0)
        for node, dist in edges[current].items():
            if node not in unvisited:
                continue
            if (new := dists[current] + dist) < dists.get(node, float("inf")):
                dists[node] = new
                unvisited.remove(node)
                bisect.insort(unvisited, node, key=lambda x: dists.get(x, float("inf")))
    return dists


def run(dists, nodes, status=0, current="AA", time=26, flow=0, res=None):
    res = {} if res is None else res
    res[status] = max(res.get(status, 0), flow)
    for node, rate in nodes.items():
        index = indices[node]
        if index & status or (ntime := time - 1 - dists[current][node]) <= 0:
            continue
        fom = ntime * rate + flow
        run(dists, nodes, index | status, node, ntime, fom, res)
    return res


regex = re.compile(
    r"^Valve ([A-Z]{2}) has flow rate=([0-9]+); "
    r"(?:tunnel leads|tunnels lead) to valve(?:s?) ([A-Z]{2}(?:, [A-Z]{2})*)\n$"
)
nodes = {}
edges = {}
with open("input16.txt") as fobj:
    for line in fobj:
        name, rate, tunnels = regex.match(line).groups()
        rate = int(rate)
        nodes[name] = int(rate)
        for tunnel in tunnels.split(", "):
            edges.setdefault(name, {})[tunnel] = 1
dists = {
    node: dijkstra(nodes, edges, node)
    for node, rate in nodes.items()
    if node == "AA" or rate > 0
}
nodes = dict(filter(lambda i: i[1] != 0 or i[0] == "AA", nodes.items()))
indices = {a: 1 << i for i, a in enumerate(dists)}

print(max(run(dists, nodes, time=30).values()))
print(max(i + j for (a, i), (b, j) in com(run(dists, nodes).items(), 2) if not a & b))
