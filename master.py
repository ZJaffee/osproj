import simplejson as json
import requests

url_q1 = "http://0.0.0.0:5001/post"
url_q2 = "http://0.0.0.0:5002/post"
url_q3 = "http://0.0.0.0:5003/post"
url_q4 = "http://0.0.0.0:5004/post"

def distribute_data(li, n, m):
	# Construct the list objects
	q1 = list()
   	q2 = list()
   	q3 = list()
   	q4 = list()
   	
   	# Split into quadrants and add two extra sides on the inside of each quadrant.
   	for i in xrange(n/2+2):
   		q1.append(li[i][0:m/2+2])
   		q2.append(li[i][m/2-1::])
   	for i in xrange(n/2-1, n):
   		q3.append(li[i][0:m/2+2])
   		q4.append(li[i][m/2-1::])

   	return q1, q2, q3, q4

def calculate(q1, q2, q3, q4, n, m):

	# Serialize "List" object into a String representation of a list,
	# so we can send it over http
	q1_string = json.dumps(q1)
	q2_string = json.dumps(q2)
	q3_string = json.dumps(q3)
	q4_string = json.dumps(q4)


	# Call each of the clients and distribute the load over http
	# This process is asynchronous, as the lock is only placed on the new_q*_string variable. 
	# And in turn, is running the computations in a parallel and distributed way.
	new_q1_string = requests.post(url_q1, data=q1_string).text
	new_q2_string = requests.post(url_q2, data=q2_string).text
	new_q3_string = requests.post(url_q3, data=q3_string).text
	new_q4_string = requests.post(url_q4, data=q4_string).text

	# Deserialize the list string, and make the string a 2d list
	q1 = json.loads(new_q1_string)
	q2 = json.loads(new_q2_string)
	q3 = json.loads(new_q3_string)
	q4 = json.loads(new_q4_string)

	# Generate new grid
	li = [[0]*m for _ in range(n)]

	# add the inner portion (only one "ghost row") of each grid,
	# and add it to the new complete grid. Additonally, make sure that
	# the cells are placed back into the proper section of the whole grid.
	for i in xrange(len(q1)-1):
		for j in xrange(len(q1[0])-1):
			if q1[i][j] == 1:
				li[i][j] = 1
	for i in xrange(len(q2)-1):
		for j in xrange(1,len(q2[0])):
			if q2[i][j] == 1:
				li[i][j+m/2-1] = 1
	for i in xrange(1,len(q3)):
		for j in xrange(len(q3[0])-1):
			if q3[i][j] == 1:
				li[i+n/2-1][j] = 1
	for i in xrange(1,len(q4)):
		for j in xrange(1,len(q4[0])):
			if q4[i][j] == 1:
				li[i+n/2-1][j+m/2-1] = 1
	return li

def main():
	n=0
	m=0
	steps=0
	grid = list()

	# Parse grid.txt
	with open('grid.txt') as f:
	    n, m, steps = [int(x) for x in next(f).split()] # read first line
	    for line in f: # read rest of lines
	        grid.append([int(x) for x in line.split()])
	print "Initial Grid :"
	print grid
	# Calculate each step by distributing the data and merging it back together.
   	for step in xrange(steps):
		q1, q2, q3, q4 = distribute_data(grid, n, m)
		grid = calculate(q1, q2, q3, q4, n, m)
		print "Conway's step", step+1, ":"
		print grid


  
if __name__== "__main__":
	main()
