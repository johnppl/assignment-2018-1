def createdict():
 no = sum(1 for line in open('example graph.txt', 'r'))
 f=open('example graph.txt','r')
 D=dict()
 for i in range (1,no+1):
  L=f.readline()

  D[(L[0],L[2])]=int(L[4]+L[5])
 f.close()
 return D

def AdjacencyLists(s):
  f=open('example graph.txt','r')
  A=[]
  for i in range(1,9):
      L=f.readline()
      if s==L[0] :
          A.append(L[2])
      if s==L[2]:
          A.append(L[0])
  return A
  f.close()   


def visited():
  f=open('example graph.txt','r')
  A=[]
  no = sum(1 for line in open('example graph.txt', 'r'))
  for i in range (1,no+1):
      L=f.readline()

      if L[0] not in A:
       A.append(L[0])
      if L[2] not in A:
       A.append(L[2])
  return(A)
  f.close()




def graph():
    g=dict()
    nodes=visited()
    for v in nodes :
        g[v]=set(AdjacencyLists(v))
    print(g)


def dfs_paths(graph, start_node, end_node):
    stack = [(start_node, [start_node])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == end_node:
                yield path + [next]
            else:
                stack.append((next, path + [next]))
    return stack
 
 
     
def distpath(path):
    #Create matrix of distances
    D=createdict()
    L=[]
    for i in range(0,len(path)-1):
        L.append(D[(path[i],path[i+1])])

    return L

def findshortest(paths,b):
    L=[]
    for path in paths:
       L.append(sum(distpath(path))*b+(distpath(path)[0])*(1-b))

    x=L.index(min(L))
    return paths[x]
    


def psychology(s,t,b):
    M=[s]
    while t not in M:
        paths=AllSimplePaths(s,t)
        path=findshortest(paths,b)
        s=path[1]
        M.append(s)

    print(M,sum(distpath(M)))
