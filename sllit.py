def split(str1,separator,maxsplit):
    i = 0;
    j = 0;
    k = 0;
    list1 = []
    while k < maxsplit:
        while (str1[j] != separator):
            j += 1
        str2 = str1[i:j]
        list1.append(str2)
        print(list1) 
        j = j +1 
        i = j
        if(j == (len(str1)-1)):
            list.append(str1[i:]);
            break;
       
        k += 1
    
split("Tatev aaa aaa"," ",3) ## problem during the last string appending

