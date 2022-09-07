# implementation of BFS

import collections
def bfs(graph,root):   # BFS usees Queue data structure fro internal operation
	visited = set()    #  
	queue = collections.deque([root])
	while queue:
		vertex = queue.popleft()  # first in first out
		visited.add(vertex)       # add vertex to the visited set
		for i in graph[vertex]:
			if i not in visited:
				queue.append(i)

	print(visited)


if __name__ == '__main__':
	graph = {             # representing graph as a dictionary order        
       
              0:[1,2,3],
              1:[0,2],
              2:[0,1,4],
              3:[0],
              4:[2]  }
bfs(graph,0)  # function calling

'''   
output:
python BFS.py
{0, 1, 2, 3, 4}
                        '''