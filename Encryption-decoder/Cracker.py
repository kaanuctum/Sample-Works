import time

#the word object
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




#the cracker object
class Cracker:
    def __init__(self,language,text, timed = True):
        #set up the required objects
        self.start_time = time.time()
        self.last_step_time = time.time()
        self.solved_text = str()
        self.dictionary = list()
        self.words = list()
        self.text = list()
        self.text_string = str()
        self.certain_pairs = list() #(real, encoded)
        self.alphabet = ['a','b','c','d','e','f','g',
                         'h','i','j','k','l','m','n','o','p',
                         'q','r','s','t','u','v',
                         'w','x','y','z']
        self.alphabet_lookup = list()
        for i in range(len(self.alphabet)):
            ls = list()
            self.alphabet_lookup.append(ls)
        self.solved = False

        #divide the dictionary by length, so
        #we have to check less words later on
        for i in range(16):
            section = list()
            self.dictionary.append(section)
        if timed == True:
            print('created the dictionary', time.time()-self.last_step_time)
            self.last_step_time = time.time()
        else:
            print('created the dictionary')

        #open the text file
        #make all the words into lower case
        words = list()
        text_handle = open(text + '.txt', encoding = 'macintosh')
        i = 0
        for m in text_handle:
            n = m.replace('.',' ')
            m = n.replace(',',' ')
            n = m.replace(';',' ')
            m = n.replace('?',' ')
            n = m.replace('!',' ')
            m = n.replace("'",' ')
            n = m.replace('"',' ')
            m = n.replace(':',' ')
            line = m.split()
            for word in line:
                word = str(word.strip().lower())
                self.text.append(word)
                self.text_string += word
                self.text_string += ' '
                t = (word.strip().lower(), i)
                words.append(t)
                i += 1
            self.text_string += '\n'
        if timed == True:
            print('got the text file', time.time()-self.last_step_time)
            self.last_step_time = time.time()

        #convert the words in to the word object
        words.sort()
        for word ,order in words:
            tec = Word(word,order)
            tec.get_doubles
            self.words.append(tec)
            i += 1


        if timed == True:
            print('converted to word object', time.time()-self.last_step_time)
            self.last_step_time = time.time()
        else:
            print('converted to word object')

        #get the the letters that repeat in the word
        for word in self.words:
            word.get_doubles()

        if timed == True:
            print('got the doubles in the sentence', time.time()-self.last_step_time)
            self.last_step_time = time.time()
        else:
            print('got the doubles in the sentence')

        print('\n')
        print('filling in the dictionary ')
        #get all the words in the dictionary
        dictionary = open('Dictionaries/' + language + '.txt', encoding = 'macintosh')#open('german1.txt')
        for n in dictionary:
            if len(n) - 1 > 15:
                self.dictionary[15].append(n.strip().lower())
            else:
                self.dictionary[len(n) - 1].append(n.strip().lower())


        if timed == True:
            print('filled in the dictionary', time.time()-self.last_step_time)
            self.last_step_time = time.time()
        else:
            print('filled in the dictionary')


        print('\n')
        print('filling in the possibilites list for each word')
        #add the words to the possibilies
        #list of each word
        for word in self.words:
            if len(word.encrypted) < 15:
                for poss in self.dictionary[len(word.encrypted)]:
                    if word.doubles_check(poss) == True:
                        word.pos.append(poss)
            else:
                for poss in self.dictionary[15]:
                    if word.doubles_check(poss) == True:
                        word.pos.append(poss)





        if timed == True:
            print('made the possibilities list', time.time()-self.last_step_time)
            self.last_step_time = time.time()
        else:
            print('made the possibilities list')









    #prints the words that are solved
    def see_progress(self):
        txt = self.text.copy()
        for i in range(len(txt)):
            for word in self.words:
                if word.encrypted == txt[i]:
                    if word.solved == True:
                        txt[i] = '-->' + word.decrypted
        for i in txt:
            print(i)

    def see_final_result(self):
        print('\n')
        print("-------------FINAL TEXT------------")
        print(self.solved_text.strip())
        print('-----------------------------------')


    #print all the possibilities for a word
    def print_possibilities(self, _word):
        for word in self.words:
            if word.encrypted == _word:
                print('number of possibilities',len(word.pos))
                x = input('do you want to print the possibilities (Y/N) ')
                if x.lower() == 'y':
                    print(word.pos)





    def itterate(self, prn = False):
        true_possibilities = list()
        self.alphabet_lookup =list()
        possibilities = list()


        for word in self.words:
            word.make_possibilities()
        #gets the certain results
        #if a word only has one remaining possibility
        for word in self.words:
            c_pairs = word.check_certain(prn = prn)
            for c_pair in c_pairs:
                if c_pair not in self.certain_pairs:
                    self.certain_pairs.append(c_pair)
                if c_pair not in true_possibilities:
                    true_possibilities.append(c_pair)


        if prn == True:
            print('certain pairs: ',len(self.certain_pairs))

        #if a possibility of word conflicts with previously
        #certain letter pair, remove that possibility
        for word in self.words:
            if word.solved == True: continue
            new_pos = list()
            for candidate in word.pos:
                possibile = True
                for pair in self.certain_pairs:
                    for i in range(len(word.encrypted)):
                        if pair[0] == candidate[i] and pair[1] != word.encrypted[i]:possible = False
                        if pair[0] != candidate[i] and pair[1] == word.encrypted[i]:possible = False
                if possibile == True:
                    new_pos.append(candidate)
            word.pos = new_pos.copy()


        for i in range(len(self.alphabet)):
            ls = list()
            self.alphabet_lookup.append(ls)
        for word in self.words:
            word.make_possibilities()


        for word1 in self.words:
            if word1.solved == False:
                for pair in word1.possibile_pairs:
                    possibile = True
                    for word2 in self.words:
                        if pair[1] in word2.present_letters:
                            if pair not in word2.possibile_pairs:
                                possibile = False
                    if possibile == True and pair not in true_possibilities:
                        true_possibilities.append(pair)
            else:
                continue
        if prn == True:
            print('number of possibilities', len(true_possibilities))
        if len(true_possibilities) == len(self.certain_pairs):self.solved = True
        for pair in true_possibilities:
            possibile = True
            for pp in self.certain_pairs:
                if pair[0] == pp[0] and pair[1] != pp[1]:possibile = False
                if pair[0] != pp[0] and pair[1] == pp[1]:possibile = False
            if possibile == True:
                self.alphabet_lookup[self.alphabet.index(pair[1])].append(pair)
        #the look up is orginzed by what the encoded letters could be
        for word in self.words:
            new_possibilities = list()
            if word.solved == False:#only tries to remove impossible one, if it is not already solved

                for candidate in word.pos:
                    exception = False
                    for i in range(len(word.encrypted)):
                        current_possibilities = self.alphabet_lookup[self.alphabet.index(word.encrypted[i])]
                        real = candidate[i]
                        encd = word.encrypted[i]
                        t = (real,encd)
                        if t not in current_possibilities:
                            exception = True
                    if exception == False:
                        new_possibilities.append(candidate)
                word.pos = new_possibilities.copy()


    def solve(self, prn = True):
        while self.solved == False:
            sen.itterate(prn = prn)
        print('solved in',time.time() - self.start_time,'seconds')
        self.solved_text = str()
        for i in range(len(self.text_string)):
            current_letter = self.text_string[i]
            if current_letter in self.alphabet:
                self.solved_text += self.alphabet_lookup[self.alphabet.index(current_letter)][0][0]
            else:
                self.solved_text += current_letter






if __name__ == '__main__':
    sen = Cracker(language = 'german', text = 'nemessis',timed = True)
    sen.solve(prn = False)
    sen.see_final_result()
