graph = {           # Dictionary
	                # graph representation
 'A':['B','C','D'],
 'B':['E'],
 'C':['D','E'],
 'D':[],
 'E':[]
}

visited = set() # store all the visited nodes
 # function creation
def dfs(visited, graph, root):
	if root not in visited:
		print(root)
		visited.add(root)
		for neighbour in graph[root]:
			dfs(visited,graph,neighbour)  # recursive call of the function

dfs(visited,graph,'A')     # function calling 

'''
Out Put:
python DFS_on_Graph.py
A
B
E
C
D


'''