Misplaced tile
import heapq, random

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

def misplaced(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count


def neighbors(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            yield new_state

def to_tuple(state):
    return tuple(tuple(row) for row in state)


def is_solvable(flat):
    inv = 0
    nums = [x for x in flat if x != 0]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                inv += 1
    return inv % 2 == 0


def random_state():
    nums = list(range(9))
    while True:
        random.shuffle(nums)
        if is_solvable(nums):
            return [nums[0:3], nums[3:6], nums[6:9]]


def astar(start):
    open_list = [(misplaced(start), 0, start, [])]
    visited = set()

    while open_list:
        f, g, state, path = heapq.heappop(open_list)
        if state == goal:
            return path + [state]
        visited.add(to_tuple(state))
        for n in neighbors(state):
            if to_tuple(n) not in visited:
                new_g = g + 1
                heapq.heappush(open_list, (new_g + misplaced(n), new_g, n, path + [state]))
    return None

def print_state(state):
    for row in state:
        print(row)
    print()


if __name__ == "__main__":
    start = random_state()
    print("Initial Random State:")
    print_state(start)
    sol = astar(start)
    if sol:
        print("Moves needed:", len(sol)-1)
        for s in sol:
            print_state(s)
    else:
        print("No solution found.")


Manhattan
import heapq, random

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]


def manhattan(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x = (val-1)//3
                goal_y = (val-1)%3
                dist += abs(i-goal_x) + abs(j-goal_y)
    return dist


def neighbors(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            yield new_state

def to_tuple(state):
    return tuple(tuple(row) for row in state)


def is_solvable(flat):
    inv = 0
    nums = [x for x in flat if x != 0]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                inv += 1
    return inv % 2 == 0


def random_state():
    nums = list(range(9))
    while True:
        random.shuffle(nums)
        if is_solvable(nums):
            return [nums[0:3], nums[3:6], nums[6:9]]

def astar(start):
    open_list = [(manhattan(start), 0, start, [])]
    visited = set()

    while open_list:
        f, g, state, path = heapq.heappop(open_list)
        if state == goal:
            return path + [state]
        visited.add(to_tuple(state))
        for n in neighbors(state):
            if to_tuple(n) not in visited:
                new_g = g + 1
                heapq.heappush(open_list, (new_g + manhattan(n), new_g, n, path + [state]))
    return None

def print_state(state):
    for row in state:
        print(row)
    print()


if __name__ == "__main__":
    start = random_state()
    print("Initial Random State:")
    print_state(start)
    sol = astar(start)
    if sol:
        print("Moves needed:", len(sol)-1)
        for s in sol:
            print_state(s)
    else:
        print("No solution found.")


[1, 4, 2]
[7, 0, 3]
[5, 6, 8]

[1, 0, 2]
[7, 4, 3]
[5, 6, 8]

[0, 1, 2]
[7, 4, 3]
[5, 6, 8]

[7, 1, 2]
[0, 4, 3]
[5, 6, 8]

[7, 1, 2]
[5, 4, 3]
[0, 6, 8]

[7, 1, 2]
[5, 4, 3]
[6, 0, 8]

[7, 1, 2]
[5, 0, 3]
[6, 4, 8]

[7, 1, 2]
[0, 5, 3]
[6, 4, 8]

[0, 1, 2]
[7, 5, 3]
[6, 4, 8]

[1, 0, 2]
[7, 5, 3]
[6, 4, 8]

[1, 5, 2]
[7, 0, 3]
[6, 4, 8]

[1, 5, 2]
[7, 3, 0]
[6, 4, 8]

[1, 5, 2]
[7, 3, 8]
[6, 4, 0]

Goal:
[1, 2, 3]
[4, 5, 6]
[7, 8, 0]

[2, 8, 3]
[1, 6, 4]
[7, 0, 5]

[2, 8, 3]
[1, 6, 4]
[7, 5, 0]

[2, 8, 3]
[1, 6, 0]
[7, 5, 4]

[2, 8, 3]
[1, 0, 6]
[7, 5, 4]

[2, 8, 3]
[0, 1, 6]
[7, 5, 4]

[0, 8, 3]
[2, 1, 6]
[7, 5, 4]

[8, 0, 3]
[2, 1, 6]
[7, 5, 4]

[8, 1, 3]
[2, 0, 6]
[7, 5, 4]

[8, 1, 3]
[2, 5, 6]
[7, 0, 4]

[8, 1, 3]
[2, 5, 6]
[7, 4, 0]

Goal:
[1, 2, 3]
[4, 5, 6]
[7, 8, 0]

