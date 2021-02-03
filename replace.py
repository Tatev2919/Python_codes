def replace(str1,oldval,newval,count):
    k = len(oldval)
    replacedStr = ""
    count1 = count
    
    for j in range(len(str1)-k +1):
        for i in range(j,len(str1)-k+1):
            if(str1[j:j+k] == oldval):
                if(count1 == count): 
                    replacedStr = str1[:j] + newval + str1[j+k:];
                    print(replacedStr)
                    count1 -=1
                    print(j)
                    break
                else:
                    replacedStr = replacedStr[:j-2] + newval + str1[j+k:];
        if(count == 0):
            break
    return replacedStr
    
    
print(replace("This is a Stringand String 111","String","char",3))
