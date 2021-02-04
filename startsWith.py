def startswith(str1,substr):
    lengthS = len(substr)
    if str1[:lengthS] == substr:
        return True
    return False
print(startswith("this isss","this"))
