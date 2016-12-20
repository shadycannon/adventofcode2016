#!/usr/bin/python

inp = open('2_input', 'r').readlines()
keypad = [[1,4,7], [2,5,8], [3,6,9]]

#custom add 1 and sub 1 functions
def add(num):
  if num == 2:
    return 2
  else:
    return num + 1

def sub(num):
  if num == 0:
    return 0
  else:
    return num - 1

def get_next_key(start, string):
  for c in string:
    if c == 'U':
      start[1] = sub(start[1])
    if c == 'D':
      start[1] = add(start[1])
    if c == 'L':
      start[0] = sub(start[0])
    if c == 'R':
      start[0] = add(start[0])
  return start
   

def part1(start, inp):
  sequence = ""
  for string in inp:
    key_coord = get_next_key(start, string)
    start = key_coord
    sequence += str(keypad[key_coord[0]][key_coord[1]])
  print sequence 

    
########################################################################
#list of coords allowed to move in a certain direction. 
up = [[2,1],[1,2],[2,2],[3,2],[1,3],[2,3],[3,3],[2,4]]
down = [[2,0],[1,1],[2,1],[3,1],[1,2],[2,2],[3,2],[2,3]]
left = [[1,2],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3],[4,2]]
right = [[0,2],[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,2]]
keypad2 = [
  ['x', 'x', '1', 'x', 'x'],
  ['x', '2', '6', 'A', 'x'],
  ['1', '3', '7', 'B', 'D'],
  ['x', '4', '8', 'C', 'x'],
  ['x', 'x', '9', 'x', 'x']]
  
def get_next_key_2(start, string):
  for c in string:
    if c == 'U' and start in up:
      start[1] -= 1
    if c == 'D' and start in down:
      start[1] += 1
    if c == 'L' and start in left:
      start[0] -= 1
    if c == 'R' and start in right:
      start[0] += 1
  return start

def part2(start, inp):
  sequence = ""
  for string in inp:
    key_coord = get_next_key_2(start, string)
    start = key_coord
    sequence += str(keypad2[key_coord[0]][key_coord[1]])
  print sequence 

part1([1,1], inp)
part2([4,2], inp)
