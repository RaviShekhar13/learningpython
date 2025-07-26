print("Kruskal's Algorithm - Week-05 implementation")

for i in range(5,1,-1):
    print(i)

WAdj = {}

def Kruskals(WList:dict):
    edges,components,TE=[],{},[]
    for u in WList.keys():
        edges.extend([(d,u,v) for (v,d) in WList[u]])
        components[u]=u
    edges.sort()

    for (d,u,v) in edges:
        if components[u] != components[v]:
            TE.append((u,v))
            c = components[u]
            for k in WList.keys():
                if components[k]==c:
                    components[k]=components[v]
    return TE

