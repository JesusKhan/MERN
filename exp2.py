def caesarCipherEncrypt(a, key):
    encrpytMessage=""
    for x in range (0,len(a)):
        encrpytMessage+=(chr(ord(a[x])+key))
    return encrpytMessage

def caesarCipherDecrypt(a, key):
    encrpytMessage=""
    for x in range (0,len(a)):
        encrpytMessage+=(chr(ord(a[x])-key))
    return encrpytMessage

def encrpytTransposition(a):
    cipherText = []
    for i in range(len(a)):
        if(i % 2 == 0):
            cipherText.append(a[i])
    for i in range(len(a)):
        if(i % 2 == 1):
            cipherText.append(a[i])
    return ("".join(cipherText))

def decrpytTransposition(a):
    decipherText = []
    for i in range(len(a) // 2):
        b = len(a) // 2
        decipherText.append(a[i])
        decipherText.append(a[i + b])
    return ("".join(decipherText))
        

text = "orangeisbest"

print("Original Text:  ", text)
print("Caesar Cipher Encrypted Text: ", caesarCipherEncrypt(text, 3))

res1 = caesarCipherEncrypt(text, 3)
print("Keyless Transposition Encrypted Text: ", encrpytTransposition(res1))

res2 = encrpytTransposition(res1)
print("Keyless Transposition  Decrypted Text: ", decrpytTransposition(res2))

res3 = decrpytTransposition(res2)
print(res3)
print("Caesar Decrypted Text (Original): ", caesarCipherDecrypt(res3, 3))
