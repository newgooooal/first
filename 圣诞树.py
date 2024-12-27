import networkx as nx
import matplotlib.pyplot as plt
import random

# 创建一个空的有向图
G = nx.DiGraph()

# git status
# 绿色为 Untracked files
# 红色为 Modified files
# 蓝色为 Staged files
# 黄色为 Unmerged files
# 灰色为 Unstaged files

# 生成10个随机节点
nodes = [f"Node_{i}" for i in range(10)]
G.add_nodes_from(nodes)

# 生成3个随机关系
edges = []
for _ in range(3):
    src = random.choice(nodes)
    dest = random.choice(nodes)
    while src == dest:
        dest = random.choice(nodes)
    edges.append((src, dest))

G.add_edges_from(edges)

# 绘制知识图谱
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=15, font_color="black", font_weight="bold", edge_color="gray")
plt.title("Randomly Generated Knowledge Graph")
plt.show()