#!/usr/bin/python
import re



def get_code(string):
  return int(re.search(r'\d+', string).group())

def get_checksum(string):
  cs = re.search(r'\[.*\]', string).group()
  return cs[1:6]

def sort_letters(string):
  ret_list = []
  letters = ""
  for c in string:
    if c.isdigit():
      break
    if c != "-":
      letters += c
  sl = set(letters)
  for l in sl:
    tup = (letters.count(l) * -1,l)
    ret_list.append(tup)
  ret = "".join([x for (y,x) in sorted(ret_list)][:5])
  return ret

def get_letters(room_string):
  letters = ""
  for c in room_string:
    if c.isdigit():
      break
    letters += c
  return letters

def get_valid_rooms():
  added_codes = 0
  valid_rooms = []
  for room_string in inputs:
    if sort_letters(room_string) == get_checksum(room_string):
      valid_rooms.append(room_string)
  return valid_rooms

def get_added_codes():
  valid_rooms = get_valid_rooms()
  added_codes = 0
  for room_string in valid_rooms:
    added_codes += get_code(room_string)
  return added_codes
     
def get_storage_room():
  alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']    
  valid_rooms = get_valid_rooms()
  for room_string in valid_rooms:
    shift_num = get_code(room_string) % 26 
    output = ""
    for c in get_letters(room_string):
      if c == "-":
        output += " " 
      else:
        output += alphabet[(alphabet.index(c) + shift_num)%26]
    if output == "northpole object storage ":
      return get_code(room_string)

inputs = open('4_input', 'r').readlines()
print get_added_codes()
print get_storage_room()
