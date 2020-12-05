# part 1
# -----------------------------

# n = input('start\n')
# entries = []
# while n != 'end':
#   if n == '' or not entries:
#     entries.append(n)
#   else:
#     entries[-1] = entries[-1] + ' ' + n
#   n = input()

# valid = 0
# conds = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']   # cid (country id) is optional

# for entry in entries:
#   if all([cond in entry for cond in conds]):
#     valid += 1

# print(valid)

# part 2
# ----------------------------
import re

n = input('start\n')
entries = []
while n != 'end':
  if n == '' or not entries:
    entries.append(n)
  else:
    entries[-1] = entries[-1] + ' ' + n
  n = input()

data = []

# regex patterns
hcl_reg = re.compile(r'#[0-9a-f]{6}')
pid_reg = re.compile(r'(\d{9})(?!\S)')
hgt_reg = re.compile(r'(\d{,3})(cm|in)')

# get keyval pairs
for entry in entries:
  passport = {}
  pairs = entry.split()
  for pair in pairs:
    key, val = pair.split(':')
    passport[key] = val
  data.append(passport)

valid = 0
conds = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']   # cid (country id) is optional

for p in data:
  if all([cond in list(p.keys()) for cond in conds]):
    byr = int(p['byr'])
    iyr = int(p['iyr'])
    eyr = int(p['eyr'])
    hgt = hgt_reg.search(p['hgt'])
    hcl = hcl_reg.match(p['hcl'])
    ecl = p['ecl']
    pid = pid_reg.match(p['pid'])

    # the unsightly if nest
    if 1920 <= byr <= 2002:
      if 2010 <= iyr <= 2020:
        if 2020 <= eyr <= 2030:
          if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            if hcl:
                if pid:
                  if hgt:
                    unit = hgt.group(2)
                    n = int(hgt.group(1))
                    if (unit == 'cm' and n in range(150,194)) or (unit == 'in' and n in range(59,77)):
                      valid += 1

print(valid)
