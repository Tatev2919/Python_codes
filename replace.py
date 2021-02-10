def replace(str1,oldval,newval,count):
    k = len(oldval)
    if(count <= 0):
        return str1
    for j in range(len(str1)-k +1):
            if(str1[j:j+k] == oldval):
                count-=1;
                str1 = str1[:j] + newval + str1[j+k:];
            if (count == 0):
                break
    return str1

print(replace("This is a Stringand String 11 sdds sf sd String","String","char",2))
