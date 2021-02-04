
def title(str1):
    str2 = list(str1)
    for i in range(len(str2)):
        if(ord(str2[i-1]) >= 32) &(ord(str2[i-1] )<= 48):
            if (ord(str2[i]) >= 97) & (ord(str2[i]) <= 123):
                str2[i] = chr(ord(str1[i])-32)
        else:
            if( ord(str2[i]) >=65) & (ord(str2[i]) <91):
                str2[i] = chr(ord(str1[i])+32)
    str1 = "".join(str2)
    return str1

print(title("this iSn't ****aAa "))
