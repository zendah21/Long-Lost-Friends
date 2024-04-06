import copy

import numpy as np
import queue as Queue


FILENAME = "sources.txt"
def get_map(filename=FILENAME):
    file = open(filename,"r")
    the_map =[]
    lines = file.read()
    rows = lines.split(',')
    print(rows)
    return the_map

def extend_path(main_path):
    path_extensions = [move_upwards(main_path), move_downwards(main_path), move_rightwards(main_path), move_leftwards(main_path)]
    return path_extensions

def move_upwards(path_list):
    move_up = copy.deepcopy(path_list)
    last_block = copy.deepcopy(path_list[-1])
    move_up.append(last_block)
    move_up[-1][1] = move_up[-1][1] + 1
    move_up[-1][-1] = move_up[-1][-1] + 1
    return move_up

def move_downwards(path_list):
    move_down = copy.deepcopy(path_list)
    last_block = copy.deepcopy(path_list[-1])
    move_down.append(last_block)
    move_down[-1][1] = move_down[-1][1] - 1
    move_down[-1][-1] = move_down[-1][-1] + 1
    return move_down

def move_leftwards(path_list):
    move_left = copy.deepcopy(path_list)
    last_block = copy.deepcopy(path_list[-1])
    move_left.append(last_block)
    move_left[-1][0] = move_left[-1][0] - 1
    move_left[-1][-1] = move_left[-1][-1] + 1
    return move_left

def move_rightwards(path_list):
    move_right = copy.deepcopy(path_list)
    last_block = copy.deepcopy(path_list[-1])
    move_right.append(last_block)
    move_right[-1][0] = move_right[-1][0] + 1
    move_right[-1][-1] = move_right[-1][-1] + 1
    return move_right


def A_search(the_map):
    # assume that path = [nodeA, nodeB, length]
    queue = []
    start_index = the_map.index('A')
    main_path = [[0, 0, 0]]
    while not len(queue) == 0:
        if the_map(main_path[0], main_path[1]) in ['A', 'B', 'C', 'D'] :
            return 'success'
        main_path = queue.pop(0)
        for extended_path in extend_path(main_path):
            queue.append(extended_path)





if __name__ == '__main__':

    the_map = get_map(FILENAME)


