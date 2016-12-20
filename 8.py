#!/usr/bin/python

DIMX = 50
DIMY = 6

screen = []
for x in range(DIMX):
  tmp = []
  for y in range(DIMY):
    tmp.append('.')
  screen.append(tmp)


def print_screen():
  for y in range(DIMY):
    linestr = ""
    for x in range(DIMX):
      linestr +=  screen[x][y]
    print linestr

def parse_input(line):
  dirs = line.split()
  if dirs[0] == "rect":
    return (0, int(dirs[1].split('x')[0]), int(dirs[1].split('x')[1]))
  elif dirs[1] == "row":
    return (1, int(dirs[4]), int(dirs[2].split('=')[1])) 
  else:
    return (2, int(dirs[2].split('=')[1]), int(dirs[4])) 

def rect(X,Y):
  for y in range(Y):
    for x in range(X):
     screen[x][y] = '#' 
 
def column(X,Y):
  old_col = screen[X]
  new_col = old_col[-1*Y:] + old_col[:-1*Y] 
  screen[X] = new_col

def row(X,Y):
  old_row = ""
  for column in screen:
    old_row += column[Y] 
  new_row = old_row[-1*X:] + old_row[:-1*X]
  for i in range(len(new_row)):
    screen[i][Y] = new_row[i]

def count_hashes():
  count = 0
  for column in screen:
    for pixel in column:
      if pixel == '#':
        count += 1
  return count

input = open('input_8', 'r')
for line in input:
  func_id,X,Y =parse_input(line)
  if func_id == 0:
    rect(X,Y)
  elif func_id == 1:
    row(X,Y)
  else:
    column(X,Y)
print_screen()
print count_hashes()
