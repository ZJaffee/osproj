from flask import Flask
from flask import request
app = Flask(__name__)
import simplejson as json

## This is to check if the client is running
@app.route("/")
def up():
	return 'up'

## This mehod is used for computing the result of the grid
@app.route("/post", methods=['POST'])
def compute():
	li = request.data
	q = json.loads(li)
	new_q = [[0]*len(q) for _ in range(len(q[0]))]
	for i in xrange(len(q)):
		for j in xrange(len(q[0])):
			count = conways_count(q, i, j, len(q[i]), len(q))
			if q[i][j] == 0 and count == 3:
				new_q[i][j] = 1
			elif q[i][j] == 1 and (count == 2 or count == 3):
				new_q[i][j] = 1
	return json.dumps(new_q)

## Create a tuple list of all possible nearest neighbors to x,y
def neighbors(x, y, m, n):
	neighbor = [(x2, y2) for x2 in range(x-1, x+2)
                               for y2 in range(y-1, y+2)
                               if (-1 < x < m and
                                   -1 < y < n and
                                   (x != x2 or y != y2) and
                                   (0 <= x2 < m) and
                                   (0 <= y2 < n))]
	return neighbor

## Takes the list from neighbors and counts the neighbors of the index
def conways_count(li, i, j, m, n):
	count = 0
	for x,y in neighbors(i,j,m,n):
		count = count + li[x][y]

	return count

#Expose unique port for this client
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
