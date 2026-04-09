from math import dist


def read_points(filename):
    points = []
    with open(filename) as f:
        for line in f:
            if line.strip():
                x, y = map(float, line.replace(',', '.').split())
                points.append((x, y))
    return points


def is_close(p1, p2, limit):
    return dist(p1, p2) <= limit


def build_graph(points, limit):
    n = len(points)
    graph = [[] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if is_close(points[i], points[j], limit):
                graph[i].append(j)
                graph[j].append(i)

    return graph


def dfs(v, graph, used, component):
    used[v] = True
    component.append(v)

    for u in graph[v]:
        if not used[u]:
            dfs(u, graph, used, component)


def find_clusters(points, limit=3.2):
    graph = build_graph(points, limit)
    n = len(points)
    used = [False] * n
    clusters = []

    for v in range(n):
        if not used[v]:
            component = []
            dfs(v, graph, used, component)
            cluster = [points[i] for i in component]
            clusters.append(cluster)

    return clusters


def is_normal_point(point, cluster):
    for other in cluster:
        if point != other and dist(point, other) <= 1:
            return True
    return False


def remove_anomalies(cluster):
    good_points = []

    for point in cluster:
        if is_normal_point(point, cluster):
            good_points.append(point)

    return good_points


def clean_clusters(clusters):
    result = []

    for cluster in clusters:
        cleared = remove_anomalies(cluster)
        if cleared:
            result.append(cleared)

    return result


def cluster_distances(clusters):
    dmin = float('inf')
    dmax = 0

    for i in range(len(clusters)):
        for j in range(i + 1, len(clusters)):
            for p1 in clusters[i]:
                for p2 in clusters[j]:
                    d = dist(p1, p2)
                    dmin = min(dmin, d)
                    dmax = max(dmax, d)

    return int(dmin * 10000), int(dmax * 10000)


def solve(filename):
    points = read_points(filename)
    clusters = find_clusters(points)
    clusters = clean_clusters(clusters)
    return cluster_distances(clusters)


print(*solve('A.txt'))
print(*solve('B.txt'))