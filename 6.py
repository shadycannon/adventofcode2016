#!/usr/bin/python

msgs = [x.strip() for x in open('6_input', 'r').readlines()]
cols = [[], [], [], [], [], [], [], []]
#if we're in part1, we'll change all the number counts to negative so the sorted function returns the correct order
PART1 = -1
PART2 = 1


def get_sorted_list(part):
  for msg in msgs: 
    for i in range(len(msg)):
      cols[i].append(msg[i])
  sorted_list = []
  for col in cols:
    set_col = set(col)
    tups = []
    for letter in set_col:
      tups.append((col.count(letter) * part, letter))
    sorted_list.append(sorted(tups)[0])
  return sorted_list

def parse_list(sorted_list):
  output = ""
  for tup in sorted_list:
    output += tup[1]
  print output

parse_list(get_sorted_list(PART1))
parse_list(get_sorted_list(PART2))
