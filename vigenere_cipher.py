baseAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print ("Vigenere Cipher encrypter")
plainText = raw_input("Please enter the plain text: ")
key = raw_input("Please enter the key: ")
keys = []
keyLength = 0
while keyLength < len(plainText):
    for char in key:
        if keyLength < len(plainText):
            keys.append(str(char))
            keyLength = keyLength + 1
CipherText = [] 
cipherIndexValue = 0 
keyIncrement = 0
for plainTextChar in plainText: 
        #Adds the base alphabets index value of the key and the plain text char
        cipherCharIndexValue = baseAlphabet.index(keys[keyIncrement]) + baseAlphabet.index(plainTextChar) 
        while cipherIndexValue > 25:
            cipherIndexValue = cipherIndexValue - 26 
        CipherText.append(baseAlphabet[cipherIndexValue])
        keyIncrement = keyIncrement + 1
print ''.join(CipherText)
