def partition(str1,pStr):
    m = len(pStr)
    tuple1 = ();
    tuple2 = ();
    tuple3 = ();
    for i in range(len(str1)-m):
        if(str1[i:i+m] == pStr):
            tuple1 = str1[:i];
            tuple2 = pStr;
            tuple3 = str1[i+m:]
    tuple4 = (tuple1,tuple2,tuple3)
    return tuple4
print(partition("I don't know what is it ","what"))
