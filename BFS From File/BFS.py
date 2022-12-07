from FunctionBfs import bfs
import ast
with open('graph.txt') as f:
    data = f.read()
    nodes=ast.literal_eval(data)
graph=nodes
s=bfs(graph,'A','G')
print("path--->",s)



