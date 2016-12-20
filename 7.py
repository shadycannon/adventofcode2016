#!/usr/bin/python


def is_abba(string):
  for i in range(len(string) - 3):
    chunk = string[i:i+4]
    if chunk[0] == chunk[3] and chunk[1] == chunk[2] and chunk[0] != chunk[1]:
      return True
  return False


def split_up_string(string):
  inside = ""
  outside = ""
  open_bracket = False
  for c in string:
    if c == '[':
      open_bracket = True
      outside += " "
    elif c == ']':
      open_bracket = False
      inside += " "
    elif open_bracket:
      inside += c
    else:
      outside += c
  return (inside.split(), outside.split())


def count_abba_ips():
  f = open('7_input', 'r')
  input = f.readlines()
  count = 0
  for ip in input:
    inside, outside = split_up_string(ip.strip())
    inside_abba = False
    outside_abba = False
    for i in inside:
      if is_abba(i):
        inside_abba = True
        break
    for o in outside:
      if is_abba(o):
        outside_abba = True
        break
    if not inside_abba and outside_abba:
      count += 1
  return count

def get_aba(string):
  chunks = []
  for i in range(len(string) - 2):
    chunk = string[i:i+3]
    if chunk[0] == chunk[2] and chunk[0] != chunk[1]:
      chunks.append(chunk)
  return chunks
  
def count_aba_ips():
  f = open('7_input', 'r')
  input = f.readlines()
  count = 0
  for ip in input:
    inside, outside = split_up_string(ip.strip())
    inside_chunks = []
    outside_chunks = []
    for i in inside:
      inside_chunks += get_aba(i)
    for o in outside:
      outside_chunks += get_aba(o)
    aba = False
    for ic in inside_chunks:
      if not aba:
        for oc in outside_chunks:
          if ic[0] == oc[1] and ic[1] == oc[0]:
            count += 1
            aba = True
            break
  return count

print count_abba_ips()
print count_aba_ips()
