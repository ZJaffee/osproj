==
Setup and Installation:
==
In order to deploy the distributed conway's game of life, you will need to run following commands, note that there are some required dependencies in order to run this, such as flask and python2. 
    bash run.sh
    python master.py
Make sure to wait until the compute nodes are up and running before running the master file.

**master.py:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This file is the meat of the program, and is where the grid is read, split up and distributed to the different nodes. Additionally, master.py recombines the data sent back from the workers at each step, and prints out the result. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It should be noted that the divisions used contain an extra two rows/columns beyond the exact divided partition is to insure correctness at each step. 


**client1.py**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This is where the calculations happen for each quarter of the board. This is done by iterating over all of the various squares in the grid and determining the number of neighbors nearby, and acting appropriately. This quarter represents the upper left

**client2.py**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This quarter represents the upper right

**client3.py**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This quarter represents the bottom left

**client4.py**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This quarter represents the bottom right

**grid.txt:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This is the specification for the conway's game of life board. The way this works is in the first line of the file, you list the number of rows, then the number of columns, and then the number of steps you'd like to take on the board. Following that is a grid of ones and zeros that make up the board the size specified above.

**run.sh**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This is a simple file that can be used to startup all of the clients as a background task

**output**

    osproj $python master.py 
    Initial Grid:
    [[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
    Conway's step 1 :
    [[0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 1, 0, 1, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
    Conway's step 2 :
    [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
    Conway's step 3 :
    [[0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1], [0, 0, 1, 1, 1], [0, 0, 0, 0, 0]]
    
**Constraints**

Note that the grid size must be larger than 4x4 in order for the program to work. 
