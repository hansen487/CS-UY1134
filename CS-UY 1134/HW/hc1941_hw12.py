import time
start_time = time.time()

Scores={}
import string
for c in string.ascii_lowercase:
    Scores[c]=1
for c in string.ascii_uppercase:
    Scores[c]=2

def lcsScores(string1, string2, Scores, D=None, one = 0, two = 0):
    if D == None:
        D = {}
        for c in string1:
            if c not in Scores:
                string1 = string1.replace(c, '')
        for c in string2:
            if c not in Scores:
                string2 = string2.replace(c, '')
    if (one, two) in D:
        return D[(one, two)]
    if len(string1) == one or len(string2) == two:
        return ('', 0)
    if string1[one] != string2[two]:
        try1 = lcsScores(string1, string2, Scores, D, one + 1, two)
        try2 = lcsScores(string1, string2, Scores, D, one, two + 1)
        if try1[1]>try2[1]:
            D[(one, two)] = try1
            return D[(one, two)]
        else:
            D[(one, two)] = try2
            return D[(one, two)]
    else:
        t = lcsScores(string1, string2, Scores, D, one + 1, two + 1)
        D[(one, two)] = (string1[one] + t[0], Scores[string1[one]] + t[1])
        return D[(one, two)]
    
S1="""
  From fairest creatures we desire increase,
  That thereby beauty's rose might never die,
  But as the riper should by time decease,
  His tender heir might bear his memory:
  But thou, contracted to thine own bright eyes,
  Feed'st thy light's flame with self-substantial fuel,
  Making a famine where abundance lies,
  Thy self thy foe, to thy sweet self too cruel:
  Thou that art now the world's fresh ornament,
  And only herald to the gaudy spring,
  Within thine own bud buriest thy content,
  And tender churl mak'st waste in niggarding:
    Pity the world, or else this glutton be,
    To eat the world's due, by the grave and thee."""

S2="""  Look in thy glass and tell the face thou viewest
  Now is the time that face should form another;
  Whose fresh repair if now thou not renewest,
  Thou dost beguile the world, unbless some mother.
  For where is she so fair whose unear'd womb
  Disdains the tillage of thy husbandry?
  Or who is he so fond will be the tomb,
  Of his self-love to stop posterity?
  Thou art thy mother's glass and she in thee
  Calls back the lovely April of her prime;
  So thou through windows of thine age shalt see,
  Despite of wrinkles this thy golden time.
    But if thou live, remember'd not to be,
    Die single and thine image dies with thee."""

import sys
sys.setrecursionlimit(2000)
print(lcsScores(S1,S2,Scores))

print("--- %s seconds ---" % (time.time() - start_time))