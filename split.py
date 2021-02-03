def split(str1,separator,maxsplit):
    i = j = k = 0
    list1 = []
    while k < maxsplit:
        while (str1[j] != separator) and (j < len(str1)-1):
            j += 1
        if(j == len(str1)-1):
            str2 = str1[i:]
        else:
            str2 = str1[i:j]
        list1.append(str2)
        print(list1)
        j += 1
        i = j
        k += 1
        print(i,"  ",j )

split("h*a*a   "," ",2)
