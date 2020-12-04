# part 1
# --------------------------------

# n = input('start\n')
# rows = []
# while n != 'end':
#   rows.append(n)
#   n = input()

# row_len = len(rows[0])
# index = 0
# trees = 0

# while len(rows) > 1:
#   # move right 3
#   index += 3

#   # overflow to next row
#   if index >= row_len:
#     index -= row_len

#   # go down 1
#   rows.remove(rows[0])

#   try:
#     if rows[0][index] == '#':
#       trees += 1
#   except:
#     print(rows[0])
#     print("index out of range:", index)

# print(trees)

# part 2
# -------------------------------
# 
# Instructions
# -------------------------------
# Right 1, down 1.          -> 77
# Right 3, down 1.          -> 280
# Right 5, down 1.          -> 74
# Right 7, down 1.          -> 78
# Right 1, down 2.          -> 35
# 
# Product of all            -> 4355551200

n = input('start\n')
rows = []
while n != 'end':
  rows.append(n)
  n = input()

row_len = len(rows[0])
index = 0
trees = 0

# Step sizes
right_step = 1
down_step = 2

while len(rows) > down_step:
  # move right
  index += right_step

  # overflow to next row
  if index >= row_len:
    index -= row_len

  # go down
  for i in range(down_step):
    rows.remove(rows[0])

  try:
    if rows[0][index] == '#':
      trees += 1
  except:
    print(rows[0])
    print("index out of range:", index)

print(trees)
