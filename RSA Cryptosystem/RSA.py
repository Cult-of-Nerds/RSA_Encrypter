#*********
# -*- Created by Vance and Ian
# -*- https://github.com/Cult-of-Nerds
# -*- https://www.youtube.com/channel/UCCxkqK3cD49RXKsMSLGrppQ
# -*- This work is licensed under the GNU General Public License v3.0
#*********
#RSA Encryptor
p = 7793
q = 7789
n = p * q
b = 1081
a = 56137
u = 0
I = 0
d = 0
y = 0

while u == 0:
    print('Cryptography Presentation RSA Cipher Program')
    print()
    I = input("1. Encryption\n2. Decryption\nChoose(1,2): ")
    print('')
    if I == '1':
        print("---------Encrytption----------")
        print()
        x = input('Plaintext: ')
        yt = list(x)
        fg = len(x)
        d=0
        y = open('RSAC.txt','w')
        for k in range(fg):
            try:
                XY = ord(yt[d])** b %n
                #ord(XY) gives the keyboard number for XY
                
            except:
                print('ERROR 1: ENCRYPT_ONLY_LETTERS')
                x = 0
                XY = 0
            y.write(str(XY)+ ' ')
            d = d+1
        y.close()
        e = open('RSAC.txt','r')
        print(e.read())
        e.close()
    if I == '2':
        print("---------Decryption-----------")
        print()
        print('Ciphertext: ')
        hh = ''
        u = open('RSAP.txt','w')
        while hh != 'done':
            try:
                y = input()
                if y == 'done':
                    hh = 'done'
                if y != 'done':
                    YX = int(y)**a %n
                    print(chr(YX))
                #chr(YX) gives the letter of the keyboard number YX
            except:
                print('ERROR 2: DECRYPT_ONLY_ONE_NUMBER')
                y = 0
                YX = 0
        u.close()
    if I != '1' and I != '2':
        print("ERROR 3: ONLY CHOOSE 1,2")
    r = input()
    if r == 'done':
        u == 1
#Hi, Jeff
