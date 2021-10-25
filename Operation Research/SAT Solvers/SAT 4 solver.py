def xor(a,b):
    return (a or b) and (not a or not b)

def imp(a,b):
    return (not a or b)

def gdw(a,b):
    return not xor(a,b)







tot = ''
for j in range(4):
    out =  ''
    for i in range(4):
        
        p = (i == 1) or (i == 2)
        r = (j == 1) or (j == 2)
        w = j > 1
        y = i > 1


        f = (
        (p or not w) and (p or y) and (not p or not r or not w or y) and r and
         (not r or w or not y) and (w or y) and (not w or not y)
            )
                
        if f: out += 'X '
        else: out += '0 '

    tot += out + '\n'


print(tot)
