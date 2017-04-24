def comma (originalList):
    str = ""
    for i in originalList:
        str += i + ", "

    return str.strip(', ')
spam = ['apples', 'bananas', 'tofu', 'cats']
print (comma(spam))
