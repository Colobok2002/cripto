from  collections import Counter

version = 'v2'

if version == 'v1':
    slovar_rus = {
        0.090:'о',
        0.062:'(а,и)',
        0.072:'е',
        0.053:'(н,т)',
        0.040:'р',
        0.045:'с',
        0.035:'л',
        0.038:'в',
        0.028:'к',
        0.023:'п',
        0.026:'м',
        0.021 :'у',
        0.025:'д',
        0.018:'я',
        0.016:'(з,ы)',
        0.013:'г',
        0.010:'й',
        0.012:'ч',
        0.006:'(ю,ш)',
        0.009:'х',
        0.007:'ж',
        0.004:'ц',
        0.003:'(щ,э)',
        0.002:'ф',
        0.014:'(ъ/ь,б)',

    }

elif version == 'v2':

    slovar_rus = {
        9.28:'о',
        8.66:'а',
        8.10:'е',
        7.45:'и',
        6.35:'н',
        6.30:'т',
        5.53:'р',
        5.45:'с',
        4.32:'л',
        4.19:'в',
        3.47:'к',
        3.35:'п',
        3.29:'м',
        2.90:'у',
        2.56:'д',
        2.22:'я',
        2.11:'ы',
        1.90:'ь',
        1.81:'з',
        1.51:'б',
        1.41:'г',
        1.31:'й',
        1.27:'ч',
        1.03:'ю',
        0.92:'х',
        0.78:'ж',
        0.77:'ш',
        0.52:'ц',
        0.49:'щ',
        0.40:'ф',
        0.17:'э',
        0.04:'ъ',


    }

text = open('text.txt','r').read()

text = text.replace('\n',' ')

base = []
text = text.split('  ')

for i in text:
    for j in i.split(" "):
        if j != '':
            base.append(j)

base_povt = {}

for i in Counter(base):
    if version == 'v1':
        base_povt[i] = float("%.3f" % (Counter(base)[i]/len(base)))
    elif version == 'v2':
        base_povt[i] = float("%.2f" % ((Counter(base)[i] / len(base))*100))

print(base_povt)

slovar = {}

for i in base_povt:
    delta = 100
    for j in slovar_rus:
        if abs(base_povt[i]-j) < delta:
            delta = abs(base_povt[i]-j)
            letter = slovar_rus[j]
    slovar[i] = letter


otvet = ''
for i in text:
    for j in i.split(' '):
        if j != '':
            otvet += slovar[j]
    otvet += ' '

print(slovar)
print(otvet)