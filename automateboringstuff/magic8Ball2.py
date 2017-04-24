import random
messages = [ 'It is certain',
             'It is decidedly so',
             'Yes definitely so',
             'Ask again later',
             'My reply is no',
             'Outlook is not so good',
             'Very doubtful']

print( messages[random.randint(0, len(messages) - 1)])
