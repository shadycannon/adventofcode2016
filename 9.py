#!/usr/bin/python

f = open('9_input', 'r')
input_str = f.read().replace('\n','')

def decode_chunk(chunk):
  length = int(chunk[1:-1].split('x')[0])
  mult = int(chunk[1:-1].split('x')[1])
  return (length,mult)

#given a string starting with '(' this returns a chunk if it exists
def get_chunk(input_string):
  chunk = ""
  for c in input_string:
    if c != ')':
      chunk += c
    else:
      break
  chunks = chunk.split('x')
  if len(chunks) != 2:
    return False
  if chunks[0].isdigit() and chunks[1].isdigit():
    return '(' + chunk + ')'
  return False
  
  
def decompress_part1(input_str):
  i = 0
  output_str = ""
  while i < len(input_str):
    c = input_str[i]
    chunk_len = 1
    if c == '(':
      chunk = get_chunk(input_str[i+1:])
      if not chunk: 
        i += 1
        output_str += c
        continue
      decode_chunk(chunk)
      length,mult = decode_chunk(chunk)
      repeat_str = input_str[i+len(chunk):i+len(chunk)+length]
      for m in range(mult):
        output_str += repeat_str
      i += len(chunk) + length 
    else:
      output_str += c
      i += 1
  return output_str


#this function doesn't actually decompress the string, it counts how long the decompressed string is 
def decompress_part2(input_str):
  i = 0
  str_count = 0
  while i < len(input_str):
    c = input_str[i]
    chunk_len = 1
    if c == '(':
      chunk = get_chunk(input_str[i+1:])
      if not chunk: 
        i += 1
        str_count += 1
        continue
      length,mult = decode_chunk(chunk)
      repeat_str = input_str[i+len(chunk):i+len(chunk)+length]
      str_count +=  mult * decompress_part2(repeat_str)
      i += len(chunk) + length 
    else:
      str_count += 1
      i += 1
  return str_count
  
 
print len(decompress_part1(input_str))
print decompress_part2(input_str)
