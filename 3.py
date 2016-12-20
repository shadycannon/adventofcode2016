#!/usr/bin/python


def parse_input1():
  f = open('3_input', 'r')
  tri_list = []
  for line in f:
    tri_list.append([int(x) for x in line.strip().split()])
  f.close()
  return tri_list


def parse_input2():
  f = open('3_input', 'r')
  flat_list = []
  #create a flat list of all the numbers
  for line in f:
    flat_list += line.strip().split()
  i = 0
  #reorder the lists according to "column"
  reordered_list = [[], [], []]
  while i < len(flat_list):
    reordered_list[0].append(int(flat_list[i]))
    reordered_list[1].append(int(flat_list[i+1]))
    reordered_list[2].append(int(flat_list[i+2]))
    i += 3
  #flatten reordered list
  reordered_flat_list = [number for sublist in reordered_list for number in sublist]
  #split flattened list into triangles
  range_list = [x*3 for x in range(len(reordered_flat_list)/3)]
  final_list = [reordered_flat_list[x:x+3] for x in range_list]
  return final_list
  
  
    
def count_triangles(tris):
  count = 0
  for tri in tris:
    a = tri[0]
    b = tri[1] 
    c = tri[2]
    if a + b > c and b + c > a and c + a > b:
      count += 1
  return count

print count_triangles(parse_input1())
print count_triangles(parse_input2())


