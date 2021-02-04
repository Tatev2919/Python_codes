def zfill(str11,num):
    str2 = ""
    if(len(str11) < num):
        str2 = num*'0'+str11;
        return str2
    return str11

print(zfill("thig mnjhuuuuuuuu",10))
