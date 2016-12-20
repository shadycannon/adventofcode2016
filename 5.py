#!/usr/bin/python
import hashlib


def part1():
  output = ""
  index = 0
  while len(output) < 8:
    string = "reyedfim" + str(index)
    m = hashlib.md5(string)
    reyedfim_hash =  m.hexdigest()
    if reyedfim_hash[:5] == "00000":
      output += reyedfim_hash[5]
    index += 1
  return output

def is_output_full(output):
  for key in output:
    if output[key] == '.':
      return False
  return True


def part2():
  output = {'0' : '.', '1' : '.', '2' : '.', '3' : '.', '4' : '.', '5' : '.', '6' : '.', '7' : '.'}
  keys = [str(x) for x in range(8)]
  index = 0
  while not is_output_full(output):
    string = "reyedfim" + str(index)
    m = hashlib.md5(string)
    hash_string =  m.hexdigest()
    if hash_string[:5] == "00000":
      key = hash_string[5]
      value = hash_string[6]
      if key in keys:
        if output[key] == '.':
          output[key] = value
    index += 1 
  output_string = ""
  for key in keys:
    output_string += output[key]
  return output_string


print part1()
print part2()
