def split(str1,separator,maxsplit):
    i = 0;
    j = 0;
    k = 0;
    list1 = []
    while k < maxsplit:
        while (str1[j] != separator):
            j += 1
            if(j == len(str1)):
                break;
        str2 = str1[i:j]
        list1.append(str2)
        print(list1) 
        j = j +1 
        i = j
       
        
        k += 1
    
split("hhhh*aaa*aaa  ","*",1) ## problem during the last string appending

