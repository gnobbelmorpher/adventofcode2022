f = open('input.txt')
text = f.readlines()
score = 0

def scorer(first, second):
    dif = (ord(second)-ord(first) - 23)%3
    return int((dif+1)%3*3 + ord(second)-87)
    # if dif == 2:                  #hier ist die anschaulichere Variante
    #     return int(0 + ord(second) - 87)
    # elif dif == 0: 
    #     return int(3 + ord(second) - 87)
    # elif dif == 1: 
    #     return int(6 + ord(second) - 87)
    return 

for line in text:
    if line.strip() != '':
        first, second = line.split()
        score += scorer(first, second)
print(score)

#new rules: 

def chooser(first, second): 
    if second == 'X':
        return ord(first)+(ord(second)-87) 

# for line in text: 
#     if line.strip()!='':
        