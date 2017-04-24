spam = {'color': 'red', 'age': 42}
for k, v in spam.items(): # for loops in python can have multiple assignment
    print ('Key: ' + k + ' Value: ' + str(v))

    #check containment using in, not in keywords
# get() takes 2 arguments - 1: key request 2: value to give if not found
# eliminate having to check exists before requesting

picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
#'I am bringing 2 cups.'
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')
#'I am bringing 0 eggs.'

#we can set default values for specified key - use to ensure one exists
picnicItems.setdefault('basket' , 1) #there's a basket in picnic items by default

