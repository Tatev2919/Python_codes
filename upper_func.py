def upper1(str1):
    str2 = ""
    for i in str1:
        if(ord(i) > 65 and ord(i) < 91 ):
                str2 = str2 + chr(ord(i) +32)
        else:
            str2 = str2+ i
    return str2

print(upper1("TaTev"))
