def strip(str1):
    i = 0
    str2 = ""
    str3 = ""
    while str1[i]==" ":
        i += 1
        continue
    str2 = str1[i:]
    j = len(str2)-1
    while str2[j] == " ":
        j -=1
        continue
    str3 = str2[:j+1];
    return str3

print(strip("           ahh     hbc "))
