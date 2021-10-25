class Word:
    def __init__(self,encrypted, order):
        self.encrypted = encrypted
        self.solved = False
        self.decrypted = ''
        self.order = order
        self.pos = list()
        self.doubles = list()
        self.possibile_pairs = list()
        self.present_letters = list()

        #create the letters present in the encrypted version
        #of a word
        for i in range(len(self.encrypted)):
            letter = self.encrypted[i]
            if letter not in self.present_letters:
                self.present_letters.append(letter)
        
    def get_doubles(self):
        for i in range(len(self.encrypted)):
            for n in range(len(self.encrypted)):
                w = self.encrypted[i]
                W = self.encrypted[n]
                if w == W and i != n:
                    t = (i,n)
                    T = (n,i)
                    if  T not in self.doubles:
                        if t not in self.doubles:
                            self.doubles.append(t)

    def doubles_check(self, pos):
        if len(self.encrypted) != len(pos):
            res = False
        else:
            doubles = list()
            for i in range(len(pos)):
                for n in range(len(pos)):
                    w = pos[i]
                    W = pos[n]
                    if w == W and i != n:
                        t = (i,n)
                        T = (n,i)
                        if  T not in doubles:
                            if t not in doubles:
                                doubles.append(t)
            if doubles == self.doubles:
                res = True
            else:
                res = False
        return res
            
    def give_certains(self): # (real, encoded)
        certains = list()
        if len(self.pos) == 1:
            only_option = self.pos[0]
            for i in range(len(only_option)):
                real = only_option[i]
                encd = self.encrypted[i]

                tupl = (real,encd)
                if tupl not in certains:
                    certains.append(tupl)
        return certains


    
    def give_possibilities(self):
        poss = list()
        for word in self.pos:
            for i in range(len(word)):
                real = word[i]
                encr = self.encrypted[i]
                t = (real, encr)
                if t not in poss:
                    poss.append(t)
        return poss
    def make_possibilities(self):
        self.possibile_pairs = self.give_possibilities().copy()
    def check_certain(self, prn = False):
        
        if len(self.pos) == 1:
            self.solved = True
            self.decrypted = self.pos[0]
            pairs = list()
            if prn == True:
                print(self.encrypted, ' --> ', self.decrypted)
            for i in range(len(self.decrypted)):
                real = self.decrypted[i]
                encr = self.encrypted[i]
                t = (real, encr)
                if t not in pairs: pairs.append(t)
            self.possible_pairs = pairs.copy()
        else:
            pairs = list()
        return pairs





if __name__ == '__main__':
    word = Word('zkzzkz',0)
    word.get_doubles()
    pos = word.give_possibilities()
    for p in pos:
        print(p)




    
            
