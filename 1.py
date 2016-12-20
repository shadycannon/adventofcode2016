#!/usr/bin/python

steps = ['R2','L3','R2','R4','L2','L1','R2','R4','R1','L4','L5','R5','R5','R2','R2','R1','L2','L3','L2','L1','R3','L5','R187','R1','R4','L1','R5','L3','L4','R50','L4','R2','R70','L3','L2','R4','R3','R194','L3','L4','L4','L3','L4','R4','R5','L1','L5','L4','R1','L2','R4','L5','L3','R4','L5','L5','R5','R3','R5','L2','L4','R4','L1','R3','R1','L1','L2','R2','R2','L3','R3','R2','R5','R2','R5','L3','R2','L5','R1','R2','R2','L4','L5','L1','L4','R4','R3','R1','R2','L1','L2','R4','R5','L2','R3','L4','L5','L5','L4','R4','L2','R1','R1','L2','L3','L2','R2','L4','R3','R2','L1','L3','L2','L4','L4','R2','L3','L3','R2','L4','L3','R4','R3','L2','L1','L4','R4','R2','L4','L4','L5','L1','R2','L5','L2','L3','R2','L2']

coords = [0,0]
allcoords = [[0,0]]
dirs = [0, 0, 0, 0]
alldirs = [[0,0,0,0]]
index = 0
first_intersect = False
for step in steps: 
  if 'R' in step: 
    index += 1
    index %= 4
  elif 'L' in step: 
    index -= 1
    index %= 4
  for i in range(int(step[1:])):
    dirs[index] += 1
    if index < 2:
      coords[index % 2] += 1
    else:
      coords[index % 2] -= 1
    if not first_intersect:
      if coords in allcoords:
        first_intersect = True
        print "Part 2: HQ is {0} blocks away".format(abs(coords[0]) + abs(coords[1]))
    allcoords.append([coords[0],coords[1]])

print "Part 1: HQ is {0} blocks away".format(abs(coords[0]) + abs(coords[1]))
  
