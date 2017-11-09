# python 3

def ransom_note(magazine, ransom):
    di_mag = dict()
    di_ran = dict()
    for w in magazine:
        if w not in di_mag:
            di_mag[w] = 1
        else:
            di_mag[w] += 1
    for w in ransom:
        if w not in di_ran:
            di_ran[w] = 1
        else:
            di_ran[w] += 1
        if di_ran[w] > di_mag[w]:
            return False
    return True
    

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")