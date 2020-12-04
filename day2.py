# PART 1
# ------------------------------------

# n = input('start')
# k = []
# while n != 'end':
#   n = n.split()
#   k.append(n)
#   n = input()

# valid = 0

# for i in k:
#   rnge = i[0].split('-')
#   letter = i[1][0]
#   pswd = i[2]
#   if int(rnge[0]) <= pswd.count(letter) <= int(rnge[1]):
#     valid += 1

# print(valid)

# part2
# --------------------------------------

n = input('start')
k = []
while n != 'end':
  n = n.split()
  k.append(n)
  n = input()

valid = 0

for i in k:
  pos = i[0].split('-')
  letter = i[1][0]
  pswd = i[2]
  if int(pos[1]) <= len(pswd) and int(pos[0]) <= len(pswd):
    try:
      if (pswd[int(pos[0])-1] == letter) or (pswd[int(pos[1])-1] == letter):
        if not ((pswd[int(pos[0])-1] == letter) and (pswd[int(pos[1])-1] == letter)):
          valid += 1
    except:
      print(pos, letter, pswd)

print(valid)
