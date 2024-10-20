from settings import *
import pygame

text_map = [
    '1561126511211611611611111',  # 1
    '5.......................1',  # 2
    '3.41.161.161.31.5.1.162.1',  # 3
    '6....121...1.61.1.1.611.6',  # 4
    '4.1611...4....4.6....41.4',  # 5
    '1......1.61.1.1.1.11....3',  # 6
    '4.16...6.51.5.5.3.11354.1',  # 7
    '1.41.417.76.1...1.......2',  # 8
    '1..1..1171...11.1614123.1',  # 9
    '15.....15..1....161...1.4',  # 10
    '15.131....151.1.....4.6.3',  # 11
    '14.....15.......151.....2',  # 12
    '3...12361131.51..11121.51',  # 13
    '2.51......51......4....21',  # 14
    '1....1441....1511...31411',  # 15
    '1261411116235111142111111',  # 16
]
WORLD_WIDTH = len(text_map[0]) * WALL_SIZE
WORLD_HEIGHT = len(text_map[0]) * WALL_SIZE
world_map = {}
collision_walls = []
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            collision_walls.append(pygame.Rect(i * WALL_SIZE, j * WALL_SIZE, WALL_SIZE, WALL_SIZE))
            if char == '1':
                world_map[(i * WALL_SIZE, j * WALL_SIZE)] = '1'
            elif char == '2':
                world_map[(i * WALL_SIZE, j * WALL_SIZE)] = '2'
            elif char == '3':
                world_map[(i * WALL_SIZE, j * WALL_SIZE)] = '3'
            elif char == '4':
                world_map[(i * WALL_SIZE, j * WALL_SIZE)] = '4'
            elif char == '5':
                world_map[(i * WALL_SIZE, j * WALL_SIZE)] = '5'
            elif char == '6':
                world_map[(i * WALL_SIZE, j * WALL_SIZE)] = '6'
            elif char == '7':
                world_map[(i * WALL_SIZE, j * WALL_SIZE)] = '7'

# Start Map
start_map = [
    '888888887888888',  # 1
    '88888887.788888',  # 2
    '88888888.888888',  # 3
    '8889999...99998',  # 4
    '8899999...99999',  # 5
    '8899999...99999',  # 6
    '88999999.999998',  # 7
    '88888889.988888',  # 8
    '88888889.988888',  # 9
    '88888889.988888',  # 9
    '88888888*888888',  # 10
]
START_WORLD_WIDTH = len(start_map[0]) * WALL_SIZE
START_WORLD_HEIGHT = len(start_map[0]) * WALL_SIZE
start1_map = {}
collision_walls1 = []
for j, row in enumerate(start_map):
    for i, char in enumerate(row):
        if char != '.':
            collision_walls1.append(pygame.Rect(i * WALL_SIZE, j * WALL_SIZE, WALL_SIZE, WALL_SIZE))
            if char == '7':
                start1_map[(i * WALL_SIZE, j * WALL_SIZE)] = '7'
            elif char == '8':
                start1_map[(i * WALL_SIZE, j * WALL_SIZE)] = '8'
            elif char == '9':
                start1_map[(i * WALL_SIZE, j * WALL_SIZE)] = '1'
            elif char == '*':
                start1_map[(i * WALL_SIZE, j * WALL_SIZE)] = '*'
            elif char == '%':
                start1_map[(i * WALL_SIZE, j * WALL_SIZE)] = '%'

# Finish Map
finish_map = [
    '8888888888888888',  # 0
    '88........888888',  # 1
    '8..888888.88...8',  # 2
    '8.8.....8.88.8.8',  # 3
    '8...888.8.88.8.8',  # 4
    '98888...8.8..8.8',  # 5
    '8...8.888...8..8',  # 6
    '8.8.8.8888888.88',  # 7
    '8.8.8.8..888..88',  # 8
    '8.8...8.88...888',  # 9
    '8.88888.88.88888',  # 10
    '8.......88.8..*8',  # 11
    '9888888.88.8.888',  # 12
    '9888887.78...888',  # 12
    '9888888788888888',  # 13
]
FINISH_WORLD_WIDTH = len(finish_map[0]) * WALL_SIZE
FINISH_WORLD_HEIGHT = len(finish_map[0]) * WALL_SIZE
FINISH_map = {}
collision_walls2 = []
for j, row in enumerate(finish_map):
    for i, char in enumerate(row):
        if char != '.':
            collision_walls2.append(pygame.Rect(i * WALL_SIZE, j * WALL_SIZE, WALL_SIZE, WALL_SIZE))
            if char == '7':
                FINISH_map[(i * WALL_SIZE, j * WALL_SIZE)] = '7'
            elif char == '8':
                FINISH_map[(i * WALL_SIZE, j * WALL_SIZE)] = '8'
            elif char == '9':
                FINISH_map[(i * WALL_SIZE, j * WALL_SIZE)] = '9'
            elif char == '*':
                FINISH_map[(i * WALL_SIZE, j * WALL_SIZE)] = '*'
            elif char == '%':
                FINISH_map[(i * WALL_SIZE, j * WALL_SIZE)] = '%'
