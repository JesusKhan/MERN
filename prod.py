import string
all_letters= string.ascii_letters

print(all_letters)

def subencrypt(plain_txt,key):
    dict1 = {}
    cipher_txt=[]
    for i in range(len(all_letters)):
        dict1[all_letters[i]] = all_letters[(i+key)%len(all_letters)]
    for char in plain_txt:
        temp = dict1[char]
        cipher_txt.append(temp)
    cipher_txt= "".join(cipher_txt)
    return cipher_txt

def subdecrypt(cipher_txt,key):
    dict2 = {}
    for i in range(len(all_letters)):
        dict2[all_letters[i]] = all_letters[(i-key)%(len(all_letters))]
    subdecrypt_txt = []
    for char in cipher_txt:
        temp = dict2[char]
        subdecrypt_txt.append(temp)
    subdecrypt_txt = "".join(subdecrypt_txt)
    return subdecrypt_txt

def trnencrypt(cipher):
    str1=''
    str2=''
    count=1
    for i in cipher:
        count+=1
        if count%2==0:
            str1+=i
        else:
            str2+=i
    if(len(str1)!=len(str2)):
        str2+=' '
    lst=[]
    lst.append(str1)
    lst.append(str2)
    # print(lst)
    return lst


def trndecrypt(t1):
    str1=''
    for i in range(0,len(t1)-1):
        for j in range(0,len(t1[0])):
            str1+=t1[i][j]+t1[i+1][j]
    return str1
text = "orangeisbest"
c1 = subencrypt(text,6)
c2 = trnencrypt(c1)

print("Cipher Text After Substitution Cipher is: ",subencrypt(text,6))
print("Cipher Text After Transposition Cipher is: ",trnencrypt(c1))
print("Original Cipher Text After Substitution is : ",trndecrypt(c2))
print("Recovered plain text :", subdecrypt(trndecrypt(c2),6))