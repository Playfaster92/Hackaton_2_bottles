from copy import deepcopy

e0 = [[0,1,2],
      [3,4,5],
      [6,7,8]]

def find0(state):
    for i in range(3):
        for j in range(3):
            if state[i][j]==0:
                return i,j

def display(state):
    for row in state:
        for val in row:
            print(("#" if val==0 else val), end=" ")
        print()
    print()

def moves(place0):
    x,y = place0
    s = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    return [(a,b) for a,b in s if 0<=a and a<3 and 0<=b and b<3]

def apply_move(state, mv):
    y,x = mv
    y0, x0 = find0(e0)
    e1 = deepcopy(state)
    e1[y0][x0], e1[y][x] = e1[y][x], e1[y0][x0]
    return e1

def neighbors(state) :
    place0 = find0(state)
    return [apply_move(state, move) for move in moves(place0)]

def state_not_found(state, depths):
    return ( state not in depths[-1]  and  (len(depths)<2 or state not in depths[-2]) )

depths = [[e0]]
while depths[-1]:
    next_depth = []
    for state in depths[-1]:
        display(state)
        place0 = find0(state)
        for move in moves(place0):
            neighbor = apply_move(state, move)
            if state_not_found(neighbor, depths):
                display(neighbor)
                next_depth.append(neighbor)
    depths.append(next_depth)

print(depths)

def solve(state):
    def depth(state):
        for i in range(len(depths)):
            if state in depths[i]:
                return i
    curr = deepcopy(state)
    path = [curr]
    #display(curr)
    d = depth(curr)
    while d>0:
        for s in neighbors(curr):
            if depth(s) < d-1:
                d -= 1
                curr = s
                path.append(curr)
                break
    return path

def display_path(path):
    for state in path:
        display(state)
        print()

test = [[1,4,3],
        [6,7,2],
        [8,5,0]]

test2 = [[1,0,2],
         [3,4,5],
         [6,7,8]]

display_path(solve(test2))