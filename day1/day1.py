import numpy as np 
calories = np.genfromtxt('input.txt')

# print(calories)

f = open('input.txt')
text = f.readlines()
block = 1
maxelf = 0
sum = 0
maxcal = 0
maxcal2nd = 0
maxcal3rd = 0
for line in text:
    line = line.strip()
    if line == "":
        sum = 0
        block += 1
    else:
        sum += int(line)
        if sum >= maxcal: 
            maxcal3rd = maxcal2nd
            maxcal2nd = maxcal
            maxcal = sum
            maxelf = block

print('Maximum calories carried by any single elf: ', maxcal)
print('Calories carried by the top 3 carrying  elfes: ', maxcal+maxcal2nd+maxcal3rd)

f.close()