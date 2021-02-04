def upper(str1):
    str2 = ""
    for i in str1:
        if(ord(i) >= 97 and ord(i) < 123 ):
            str2 = str2 + chr(ord(i) -32)
        else:
            str2 = str2+ i
    return str2

print(upper("This is a string"))
