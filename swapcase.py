def swapcase(str1):
    str2 = list(str1)
    for i in range(len(str1)):
        if (ord(str2[i]) >=65) & (ord(str2[i]) <91):
            str2[i] = chr(ord(str1[i])+32)
        elif (ord(str2[i]) >= 97) & (ord(str2[i]) <= 123):
            str2[i] = chr(ord(str1[i])-32)
        else:
            str2[i] = str1[i]
    str1 = "".join(str2)
    return str1
print(swapcase("this is A String"))
