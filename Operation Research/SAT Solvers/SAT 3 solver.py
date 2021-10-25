def xor(a,b):
    return (a or b) and (not a or not b)

def imp(a,b):
    return (not a or b)

def gdw(a,b):
    return not xor(a,b)







tot = ''
for j in range(2):
    out =  ''
    for i in range(4):
        w = (i == 1 or i == 2)
        y = j == 1
        z = i == 2 or i == 3

        """
        f = (
            xor(
                (gdw(w, gdw(y,z))),
                ((y and w) or w))
            )
        """
        f = z
        
        if f: out += 'X '
        else: out += '0 '

    tot += out + '\n'


print(tot)
