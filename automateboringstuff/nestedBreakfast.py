def spam():
    eggs = 99
    baconVal = bacon() #no return val, will return None
    print (eggs)
    print (baconVal)

def bacon():
    ham = 101
    eggs = 0

spam()

def spam2():
    print (eggs)

eggs = 42
spam2()
print (eggs)
