#Segregation Simulation
 
from drawingpanel import *
from random import * 
 
#constants
GRID_SIZE = 50
AGENT_ONE = 40
AGENT_TWO = 35
PERCENTAGE = 80
SPEED = 2
 
def main(): #creates a list of list with agents and simulates until all agents are satisfied
    grid = []
    create_grid(GRID_SIZE, grid)
    p = DrawingPanel(GRID_SIZE * 10,GRID_SIZE * 10, background='white')    
    are_satisfy(grid, p)
    while (not are_satisfy(grid,p)): #while not false it will keep iterating
        are_satisfy(grid, p)
        visual (grid, p)
        p.sleep(SPEED)
 
def create_grid(GRID_SIZE, grid): #creates a list of lists
    for y in range (GRID_SIZE):
        row = [0] * GRID_SIZE
        for x in range (GRID_SIZE):
            number = randint(1,100)
            if (number <= AGENT_ONE):
                row[x] = 1
            elif (number > AGENT_ONE and number <= AGENT_ONE + AGENT_TWO):
                row[x] = 2
        grid.append(row)
 
def are_satisfy(grid, p): #checks each agent if they are satisfied, if check_neighbor returns true then move the agent and returns a boolean
    temp = True
    for row in range (0, len(grid)):
        for col in range (0, len(grid[row])):
            if check_neighbors(row, col, grid, p):
                temp = False
                move_agent(row, col, grid, p)
    return temp
 
def check_neighbors(row, col, grid, p): #checks the agents around the point and calls to is_valid helper function
    same_agents = 0
    diff_agents = 0 
    #roffset and coffset check all values around the agent
    for roffset in range (-1, 2):
        for coffset in range (-1, 2):
            offset_row = row + roffset
            offset_col = col + coffset
            if (is_valid(offset_row, offset_col)):#if it is a valid point then start counting the agents around it 
                if ((row, col) == (offset_row, offset_col) and grid[row][col] != 0):#if row, col are the same as offset_row, offset_col then nothing is added so it doesnt check itself
                    same_agents += 0
                    diff_agents += 0
                elif (grid[row][col] == grid[offset_row][offset_col] and grid[row][col] != 0):
                    same_agents += 1
                elif (grid[row][col] != grid[offset_row][offset_col] and grid[offset_row][offset_col] != 0 and grid[row][col] != 0):
                    diff_agents += 1
    total = same_agents + diff_agents
    return (total != 0 and ((same_agents / total) * 100) < PERCENTAGE) #if agent is unsatisfied, return a true boolean for check_neighbors
            
def is_valid(offset_row, offset_col): #helper function determines if the points in (offset_row, offset_col) are valid
    return (offset_row >= 0 and offset_row < GRID_SIZE and offset_col >= 0 and offset_col < GRID_SIZE) 
 
def move_agent(row, col, grid, p): #moves agent to a random blank spot, each time this helper function runs, the panel updates
    random_row = randint(0, GRID_SIZE - 1)
    random_col = randint(0, GRID_SIZE - 1)
    while (grid[random_row][random_col] != 0):
        random_row = randint(0, GRID_SIZE - 1)
        random_col = randint(0, GRID_SIZE - 1)
    grid[random_row][random_col] = grid[row][col]
    grid[row][col] = 0
 
def visual(grid, p): #outputs drawing panel of the initial list
    for i in range (1, GRID_SIZE):
        p.canvas.create_line (i * 10, GRID_SIZE * 10, i * 10, 0)
    for j in range (1, GRID_SIZE):
        p.canvas.create_line (0, j * 10, GRID_SIZE * 10, j * 10)
    for row in range (0, len(grid)):
        for col in range (0, len(grid[row])):
            if (grid[row][col] == 1):
                p.canvas.create_rectangle(row * 10, col * 10, (row + 1) * 10, (col + 1) * 10, fill= "red")
            elif (grid[row][col] == 2):
                p.canvas.create_rectangle(row * 10, col * 10, (row + 1) * 10, (col + 1) * 10, fill= "blue")
            else:
                p.canvas.create_rectangle(row * 10, col * 10, (row + 1) * 10, (col + 1) * 10, fill= "white")
main()
