
fullstr = "jashajsaj"

def func(str,start,end):
    h = 0
    flag = False
    if(len(str)>len(fullstr)):
      #  print(False)
        return False
    if (len(str) < start) | (len(str) > end):
        print(False)
        return False
    for i in range(start,end):
        flag = True
        if fullstr[i] == str[h]:
            h = h + 1
            flag = False
        if h == len(str):
            print(i-h+1)
            return i-h+1;
        elif flag: 
            h = 0;
    if h < len(str):
        print(-1," ",h)
        return -1
    
func("js",0,16);
