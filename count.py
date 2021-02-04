def count(str1,substr = " "):
    k = len(substr)
    count1 = 0
    for i in range(len(str1)-k):
        if (str1[i:i+k]==substr):
            count1 +=1
    return count1;

print(count("thisn is 0","str"))
