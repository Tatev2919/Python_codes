def replace(str1,oldval,newval,count):
    k = len(oldval)
    replacedStr = ""
    count1 = count
    for j in range(len(str1)-k +1):
        for i in range(j,len(str1)-k+1):
            if(str1[j:j+k] == oldval):
                count1-=1;
                if(count1 == count - 1):
                    str1 = str1[:j] + newval + str1[j+k:];
                    print(str1)
                    print(count1)
                    break
                else:
                    str1 = str1[:j-2*(count1)] + newval + str1[j+k:];
        if (count1 == -1):
            break
    return replacedStr


replace("This is a Stringand String 11","String","char",2)
