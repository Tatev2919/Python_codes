def strip(str1,separator=" "):
    h = 0
    str2 = str3 = ""
    flag = False
    for i in range(len(str1)):
        flag = False
        for j in range(len(separator)):
            if(str1[i] == separator[j]):
                flag = True
                h += 1
                break
        if(flag == False):
            break
    str2 = str1[h:]
    m = len(str2)
    for i in range(len(str2)-1,0,-1):
        flag = False
        for j in range(len(separator)):
            if(str2[i] == separator[j]):
                flag = True
                m -=1
                break
        if(flag == False):
            break
    str3 = str2[:m]
    return str3

print(strip("    **//?*%%/*^/*/ahh     hbc***/*/*/*^^^ "," */?%^"))
