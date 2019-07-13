from __future__ import print_function
import matplotlib.pyplot as plt
import obstacle_file

class AStarGraph(object):
	def __init__(self):
		var1 = obstacle_file.process_list()
		self.barriers = []
		testI = 0
		cordCount=1
		tplist=[]
		#for var1 in OriginalList:
		tmplist = []
		obst=input("No of obstacles ? (Should be less than equal to 6)")
		print("Full List - var1 ===========>>>>>>>>>>>>>>>>", var1)
		for cord in var1:
			print("Part of Full List - cord ===========>>>>>>>>>>>>>>>>", cord)
			print("Cord ==", cordCount)
			cordCount = cordCount + 1

			for i in cord:
				print("i ========>>>>",i)
				for j in i:
					print("j ---->>",j)
					if(testI==0):
						print("Check MEEEE  1")
						i1=j
					if (testI == 1):
						j1 = j
						print("Check MEEEE  2")
					if (testI == 2):
						i2 = j
						print("Check MEEEE  3")
					if (testI == 3):
						j2 = j
						print("Check MEEEE  4" )
					if (testI == 4):
						i3 = j
						print("Check MEEEE  5")
					if (testI == 5):
						j3 = j
						print("Check MEEEE  6")
					if (testI == 6):
						i4 = j
						print("Check MEEEE  7")
					if (testI == 7):
						j4 = j
						print("Check MEEEE  8")
					if(testI==8):
						i5=j
						print("Check MEEEE  9")
					if(testI==9):
						i6=j
						print("Check MEEEE  10")

					if(testI==9):
						testI = 0
						print("testI became 0")
					else:testI = testI + 1


			print ("i1=",i1,"j1=",j1,"i2=",i2,"j2=",j2,"i3=",i3,"j3=",j3,"i4=",i4,"j4=",j4)

			if(obst<4):
				while j1 != j2:
					print("Say hello 1")
					tmplist.append((i1, j1))
					print("(i=", i1, ",j=", j1, ")")
					j1 = j1 - 1
					'''
					if (j1 == j1):
						break
					'''
				# break

				while i2 != i3:
					print("Say hello 2")
					tmplist.append((i2, j2))
					print("(i=", i2, ",j=", j2, ")")
					i2 = i2 + 1
					print("this is decremented j1----->>", j1)
					'''
					if (i2 > i3):
						break
						'''
				# break
				while j3 != j4:
					print("Say hello 3")
					tmplist.append((i3, j3))
					print("(i=", i3, ",j=", j3, ")")
					j3 = j3 + 1
					print("this is decremented j1----->>", j1)
					'''
					if (j3 > j4):
						break
					'''
				# break
				while i4 != i1:
					print("Say hello 4")
					tmplist.append((i4, j4))
					print("(i=", i4, ",j=", j4, ")")
					i4 = i4 - 1
					print("this is decremented j1----->>", j1)
					'''
					if (i4 < i1):
						break
					'''
			# break
			else:
				while j1!=j2:

					print("Say hello 1")
					tmplist.append((i1, j1))
					print("(i=", i1, ",j=", j1, ")")
					j1=j1-1

					if (j1 == j1):
						break

					#break

				while i2 != i3:

					print("Say hello 2")
					tmplist.append((i2, j2))
					print("(i=", i2, ",j=", j2, ")")
					i2 = i2 +1
					print("this is decremented j1----->>", j1)

					if (i2 > i3):
						break

					#break
				while j3 != j4:

					print("Say hello 3")
					tmplist.append((i3, j3))
					print("(i=", i3, ",j=", j3, ")")
					j3 = j3 + 1
					print("this is decremented j1----->>", j1)
					if (j3 > j4):
						break

					#break
				while i4 != i1:
					print("Say hello 4")
					tmplist.append((i4, j4))
					print("(i=", i4, ",j=", j4, ")")
					i4 = i4 - 1
					print("this is decremented j1----->>", j1)
					if (i4 < i1):
						break
					#break
				#tplist.append(tmplist)
				#tmplist[:]=[]
			#print("This is tmplist ++++++++++",tmplist)
		print("This is tmplist -===-=====-=========-=====>>>>>>>>>>>>>>>", tmplist)
		#tplist.append(tmplist)
		self.barriers.append(tmplist)
	def heuristic(self, start, goal):
		#Use Chebyshev distance heuristic if we can move one square either
		#adjacent or diagonal
		D = 1
		D2 = 1
		dx = abs(start[0] - goal[0])
		dy = abs(start[1] - goal[1])
		return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)
 
	def get_vertex_neighbours(self, pos):
		n = []
		#Moves allow link a chess king
		for dx, dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]:
			x2 = pos[0] + dx
			y2 = pos[1] + dy
			if x2 < 0 or x2 > 1000 or y2 < 0 or y2 > 1000:
				continue
			n.append((x2, y2))
		return n
 
	def move_cost(self, a, b):
		for barrier in self.barriers:
			if b in barrier:
				return 100 #Extremely high cost to enter barrier squares
		return 1 #Normal movement cost
 
def AStarSearch(start, end, graph):
 
	G = {} #Actual movement cost to each position from the start position
	F = {} #Estimated movement cost of start to end going via this position
 
	#Initialize starting values
	G[start] = 0 
	F[start] = graph.heuristic(start, end)
 
	closedVertices = set()
	openVertices = set([start])
	cameFrom = {}
 
	while len(openVertices) > 0:
		#Get the vertex in the open list with the lowest F score
		current = None
		currentFscore = None
		for pos in openVertices:
			if current is None or F[pos] < currentFscore:
				currentFscore = F[pos]
				current = pos
 
		#Check if we have reached the goal
		if current == end:
			#Retrace our route backward
			path = [current]
			while current in cameFrom:
				current = cameFrom[current]
				path.append(current)
			path.reverse()
			return path, F[end] #Done!
 
		#Mark the current vertex as closed
		openVertices.remove(current)
		closedVertices.add(current)
 
		#Update scores for vertices near the current position
		for neighbour in graph.get_vertex_neighbours(current):
			if neighbour in closedVertices: 
				continue #We have already processed this node exhaustively
			candidateG = G[current] + graph.move_cost(current, neighbour)
 
			if neighbour not in openVertices:
				openVertices.add(neighbour) #Discovered a new vertex
			elif candidateG >= G[neighbour]:
				continue #This G score is worse than previously found
 
			#Adopt this G score
			cameFrom[neighbour] = current
			G[neighbour] = candidateG
			H = graph.heuristic(neighbour, end)
			F[neighbour] = G[neighbour] + H
	raise RuntimeError("A* failed to find a solution")
if __name__=="__main__":
	graph = AStarGraph()
	result, cost = AStarSearch((7,6), (400,300), graph)
	print ("route", result)
	print ("cost", cost)
	plt.plot([v[0] for v in result], [v[1] for v in result])
	for barrier in graph.barriers:
		for bar in barrier:
			plt.plot([v[0] for v in barrier], [v[1] for v in barrier])

	plt.xlim(0,1000)
	plt.ylim(0,1000)
	plt.show()
