import numpy as np
import matplotlib.pyplot as plt
text = "THEREARETWOWAYSOFCONSTRUCTINGASOFTWAREDESIGNONEWAYISTOMAKEITSOSIMPLETHATTHEREAREOBVIOUSLYNODEFICIENCIESANDTHEOTHERWAYISTOMAKEITSOCOMPLICATEDTHATTHEREARENOOBVIOUSDEFICIENCIESTHEFIRSTMETHODISFARMOREDIFFICULT"


def encrypt(cipher, key):
    shifted = []
    numKey = [ord(x) for x in key]
    numCipher = [ord(x) for x in cipher]
    keyCHR = 0
    for letter in numCipher:
        letter += numKey[keyCHR] - 65
        keyCHR += 1
        if keyCHR == len(key):
            keyCHR = 0
        if letter > 90:
            letter = letter - 26
        shifted.append(letter)
    encrypted = [chr(number) for number in shifted]
    encrypted = ''.join(encrypted)
    return encrypted


def countNumsInAlph(cipher):

    ic = {}
    for chr in 'ABCDEFGIJKLMNOPQRSTUVWXYZ':
        howMany = 0
        for chrInMsg in cipher:
            if chrInMsg == chr:
                howMany += 1
        ic[chr] = howMany
    return ic


def countIC(cipher):
    ic = countNumsInAlph(cipher)
    suma = 0
    for key in ic.keys():
        help = ic[key] * (ic[key] - 1)
        suma += help

    IK = sum / (len(cipher) * (len(cipher) - 1))
    return IK


def CountKappa(firstText, secondText):
    kronnecker = 0
    for char in enumerate(firstText):
        if char[1] == secondText[char[0]]:
            kronnecker += 1
    return kronnecker / len(firstText)


def countCHI(firstText, secondText):
    total = 0
    counts1 = countNumsInAlph(firstText.upper())
    counts2 = countNumsInAlph(secondText.upper())
    for char in counts1.keys():
        letter = counts1[char] * counts2[char]
        total += letter
    return total / (len(firstText)**2)


def givMeICS(cipher, maxLen):
    avg = []
    for repeat in range(maxLen):
        ICo1 = 0
        for slices in range(repeat + 1):
            sliced = cipher[slices:: repeat + 1]
            ICo1 += countIC(sliced)
        avg.append(ICo1 / (repeat + 1))
    return avg


def main():
    x = encrypt(text, 'CRYPTO')
    z = givMeICS(x, 20)

    plt.xlabel('Key length')
    plt.ylabel('IC')
    axis = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    x_pos = np.arange(len(axis))
    plt.bar(x_pos,z)
    plt.show()


if __name__ == '__main__':
    main()
