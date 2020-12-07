# part 1
# ---------------------
n = input('start\n')
codes = []
while n != 'end':
  codes.append(n)
  n = input()

ids = []

for code in codes:
  rows = list(range(128))
  columns = list(range(8))

  for i in range(7):
    if code[i] == 'F':
      rows = rows[:len(rows)//2]
    else:
      rows = rows[len(rows)//2:]
  for j in range(7, 10):
    if code[j] == 'L':
      columns = columns[:len(columns)//2]
    else:
      columns = columns[len(columns)//2:]
  ids.append(rows[0] * 8 + columns[0])

print(max(ids))

# part 2
# -----------------------

ids.sort()
your_id = set(range(ids[0], ids[-1]+1)).difference(ids).pop()

print(your_id)