def polis(POLIS = '2758620842000213'):

    sn = 0
    sh = 0


    for i in range(len(POLIS)-1):

        if i % 2 == 0:
            sh += (int(POLIS[i]) * 2) % 9
        else:
            sn += int(POLIS[i])

    if (sh + sn + int(POLIS[-1])) % 10 == 0:
        print('Контрольная цифра совпала')
    else:
        print('Контрольная цифра не совпала')


def stix(STRIH = "5901234123457"):
    sn = 0
    sh = 0

    for i in range(len(STRIH) - 1):

        if i % 2 == 0:
            sh += int(STRIH[i])
        else:
            sn += int(STRIH[i])

    sh *= 3

    if (sh + sn + int(STRIH[-1])) % 10 == 0:
        print('Контрольная цифра совпала')
    else:
        print('Контрольная цифра не совпала')

def inn(INN = '272407031780'):

    ni = 0

    if len(INN) == 10:
        mnosh= [2,4,10,3,5,9,4,6,8]
    elif len(INN) == 11:
        mnosh = [7,2, 4, 10, 3, 5, 9, 4, 6, 8]
    else:
        mnosh = [3,7,2, 4, 10, 3, 5, 9, 4, 6, 8]

    for i in range(len(INN)-1):
        ni += mnosh[i] * int(INN[i])

    ni = (ni % 11) % 10

    if ni == int(INN[-1]):
        print('Контрольная цифра совпала')
    else:
        print('Контрольная цифра не совпала')



if __name__ == '__main__':
    #polis()
    #stix()
    inn()