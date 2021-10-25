def xor(a,b):
    return (a or b) and (not a or not b)

def imp(a,b):
    return (not a or b)

def gdw(a,b):
    return not xor(a,b)







tot = ''
for j in range(4):
    out =  ''
    for i in range(8):

        q = (i == 1 or i == 2) or (i == 5 or i == 6) # A
        t = (j == 1 or j == 2) # B
        p = (1 < i < 6) # C
        s = (j > 1) # D
        r = (i > 3) # E


        f1 = (((( not q and  not t) or (p or t)) or (q and (( not t or p) and ( not p or t)))) or (((q or t) and ( not p and  not t)) and ( not q or ((t and  not p) or (p and  not t)))))

        f3 = (
            (not q or t or p)  
             )

        f4 = (t or p or not q)

        if f1: out += 'X '
        else  : out += '0 '

    tot += out + '\n'


print(tot)
