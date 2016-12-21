#!/usr/bin/python

instructions = open('10_input', 'r').readlines()
bot_dict = {}


def parse_value(i):
  bot = 'b'  + i.split()[5]
  val = int(i.split()[1])
  return (bot,val)


def parse_gives(i):
   chunks = i.split()
   giver = 'b' + chunks[1]
   rec_low = chunks[5][0] + chunks[6]
   rec_high = chunks[10][0] + chunks[11]
   return (giver,rec_low,rec_high)


def get_all_bots(instructions):
  for i in instructions:
    if "value" in i:
      bot = parse_value(i)[0]
      if bot not in bot_dict:
        bot_dict[bot] = []
    else:
      ret = parse_gives(i)
      for bot in ret:
        if bot not in bot_dict:
          bot_dict[bot] = []

get_all_bots(instructions)     
for i in instructions:
  if "value" in i:
    bot_dict[parse_value(i)[0]].append(parse_value(i)[1])
    
#arbitrary number of loops, so ugly but i hate this problem so i don't care
for j in range(50):
  for i in instructions:
    if "value" not in i: 
      giver, low, high = parse_gives(i)
      vals = bot_dict[giver]
      if len(vals) == 2:
        vals = sorted(vals)
        if vals == [17, 61]:
          print giver
        bot_dict[low].append(vals[0])
        bot_dict[high].append(vals[1])
        bot_dict[giver] = []
        instructions.remove(i)
print bot_dict['o0']
print bot_dict['o1']
print bot_dict['o2']
