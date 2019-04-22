from time import time
t=time()

ans = len("onethousand")

d1={
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine'
}

special={
    '10':'ten',
    '11':'eleven',
    '12':'twelve',
    '13':'thirteen',
    '14':'fourteen',
    '15':'fifteen',
    '16':'sixteen',
    '17':'seventeen',
    '18':'eighteen',
    '19':'nineteen'
}

d2={
    '2':'twenty',
    '3':'thirty',
    '4':'forty',
    '5':'fifty',
    '6':'sixty',
    '7':'seventy',
    '8':'eighty',
    '9':'ninety'
}

def countLetter(s):
    c = 0
    if(s[0]!='0'):
        c += len(d1[s[0]])+len("hundred")
        if(s[1:] != '00'):
            c+= len("and")
    if(s[1:] in special.keys()):
        c += len(special[s[1:]])
    else:
        if(s[1]!='0'):
            c += len(d2[s[1]])
        if(s[2]!='0'):
            c += len(d1[s[2]])
    return c

for i in range(1,1000):
    s = str(i)
    s = s.zfill(3)
    ans += countLetter(s)

print(ans)
print("Time: %s"%(time()-t))