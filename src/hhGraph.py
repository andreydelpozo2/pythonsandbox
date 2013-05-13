class Edge:
	pass

class Graph:
	def __init__(self):
		self.nodes = {}
	def addNode(self,name):
		if name in self.nodes:
			return False
		self.nodes[name] = []
	def addEdge(self, a, b,weight=1):
		self.addNode(a)
		self.addNode(b)

		e = Edge()
		e.target = b
		e.weight = weight
		self.nodes[a].append(e);

		e = Edge()
		e.target = a
		e.weight = weight
		self.nodes[b].append(e);


G = Graph()
G.addNode('a')
G.addNode('b')
G.addEdge('a','b')
G.addEdge('b','c')