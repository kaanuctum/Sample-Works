
tota,totb = '', ''
for j in range(8):
    outa, outb = '', ''
    for i in range(8):

        p = (i == 1 or i == 2) or (i == 5 or i == 6)
        q = (j == 1 or j == 2) or (j == 5 or j == 6)
        y = (i > 3)
        z = (j > 3)
        x = (1 < j < 6)
        r = (1 < i < 6)

        a = (p and ((q and (r or (not r and x and not z))) or (not q and ((r and x and z) or (not r and (x or (not x and not y and not z))))))) or (not p and ((q and ((r and x) or (not r and z))) or (
            not q and ((r and (x or (not x and (y or (not y and z))))) or (not r and x and z)))))

        b = (p and ((q and ((r and ((x and y and z) or (not x and (not y or (y and not z))))) or
            (not r and ((x and ((y and not z) or (not y and z))) or (not x and not y and not z))))) or
            (not q and not r and x and y))) or (not p and ((q and ((r and ((x and not y and not z) or (not x and y))) or (not r and x and not y and not z))) or
            (not q and ((r and not x and not y and z) or (not r and x and not y)))))


        if a: outa += 'X '
        else: outa += '0 '

        if b: outb += 'X '
        else: outb += '0 '

        
        
    tota += outa +'\n'
    totb += outb +'\n'

print('a ---------------' + '\n' + tota)
print('b ---------------' + '\n' + totb)
