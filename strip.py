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

def strip1(str1):
    str2 = str3 = ""
    i = 0
    while str1[i] == " ":
        i += 1
    str2 = str1[i:]
    j = len(str2)-1
    while str2[j] == " ":
        j -= 1
    str3 = str2[:j+1]
    print(j)
    return str3

print(strip1("      ahh   ddfd  hbc    "))
