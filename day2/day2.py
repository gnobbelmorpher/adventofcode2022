f = open('input.txt')
# f = open('input2.txt')
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

#new rules (return second in the old mannor to count): 

def chooser(first, second): 
    # loose for X, draw for Y, win for Z:
    # if second == 'Y': 
    #     return chr(ord(first)+23)
    # elif second == 'X': 
    #     return chr((ord(first)-23-1)%3 + 88)
    # elif second == 'Z':
    #     return chr((ord(first)-23+1)%3 + 88)
    return chr((ord(first) - 23 + (ord(second)-89))%3 + 88)

newscore = 0
for line in text: 
    if line.strip()!='':
        first, second = line.split()
        # print(first, second, chooser(first, second))
        newscore += scorer(first, chooser(first, second))
print(newscore)
