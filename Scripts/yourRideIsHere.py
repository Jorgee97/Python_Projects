"""
ID: android9
LANG: PYTHON3
TASK: ride
"""

fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')

comet_name = fin.readline()
group_name = fin.readline()

abc_map = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26
}


comet_name_value = 1
group_name_value = 1
for i in range(len(comet_name)):
    if comet_name[i] != '\n':
        comet_name_value *= abc_map[comet_name[i]]

for i in range(len(group_name)):
    if group_name[i] != '\n':
        group_name_value *= abc_map[group_name[i]]

if (comet_name_value % 47) == (group_name_value % 47):
    fout.write('GO' + '\n')
else:
    fout.write('STAY' + '\n')


fout.close()
