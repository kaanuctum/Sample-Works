# Simple Substitution Cipher decoder

A project for solving a riddle published in our highschool's monthly magazine.
The main premise of the riddle was that a german text was encrypted, by swapping each character of the alphabet with another random one, but keeping a consistent link between words (e.g. all 'b's are replaced with an 'a')

The given input for the riddle was the following:

  ***Bklmkgcqik jrk Ukri zrcqi Pkxrkbik,<br/>
  hdxazpk pkzmp Irzik jmgcq mzhkgk Qkgukz<br/>
  lxrkhhi<br/>
  mzj pkzmp Bxmi ndgqazjkz rhi,<br/>
  yri jky org lmkg krzazjkg jrcqikz wdkzzkz<br/>
  aml Bxakiikgz jkh Bamykh,<br/>
  jkz org jah Xkbkz um zkzzkz elxkpkz.***

The path I chose to take in solving the ridle was to go over the forms of the words. As I already knew that the text was in german, I tried a dictionary attack, where I would go and lookup all the possible words for a given form. As an example, the code would take the input 'zkzzkz' and try to find any word in the german language that had the form *121121* where the second and the fifth letter was the same and were the only different letters in the word.
After the first itteration of selecting possible pairs of encrypted letters, the second time would go over the first list of possiblities for the words, and drop any that would be in conflict with any other words. For example in the word *'zkzzkz'* there are no possible words in which the letter **'z'** might be representing the letter **'t'** in the encrypted word, so for all the other words any possiblities where such an impossible letter pair was made are dropped from the posiblities pool. This is continiued until there is only 1 possible solution for every letter. The result comes out to be:

 ***befuerchte die zeit nicht geliebte <br/>
  solange genug tinte durch unsere herzen <br/>
  fliesst <br/>
  und genug blut vorhanden ist <br/>
  mit dem wir fuer einander dichten koennen <br/>
  auf blaettern des baumes <br/>
  den wir das leben zu nennen pflegen***

