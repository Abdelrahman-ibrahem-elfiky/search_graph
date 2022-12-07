def bfs(g,start,goal):
    visited=[]
    queue=[[start]]
    while queue:
        path=queue.pop(0)
        node=path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node==goal:
            return path
        else:
            adj=g.get(node,[])
            for i in adj:
                newpath=path.copy()
                newpath.append(i)
                queue.append(newpath)

