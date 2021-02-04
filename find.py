fullstr = "jashajsaj"

def func(str,start=0,end =len(fullstr)):
    h = 0
    flag = False
    if(len(str)>len(fullstr)):
        return -1
    if (start<0) | (end > len(fullstr)):
        return -1
    for i in range(start,end):
        flag = True
        if fullstr[i] == str[h]:
            h = h + 1
            flag = False
        if h == len(str):
            return i-h+1;
        elif flag:
            h = 0;
    if h < len(str):
        return -1

print(func("js",0,8));
