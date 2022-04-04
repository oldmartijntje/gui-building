text= 'cheese. kaas is lekker? maar echt hoor? niet normaal. dusja dat is leven! cool he? maar ja! kaas. kaas.nl yeet! yeet?'
splittedDot = text.split('. ')
for x in range(len(splittedDot)-1):
    splittedDot[x] = splittedDot[x] + '.'
questionList = []
for i in range(len(splittedDot)):
    current = splittedDot[i].split('? ')
    for x in range(len(current)-1):
        current[x] = current[x] + '?'
    for x in range(len(current)):
        questionList.append(current[x])
shoutList = []
for i in range(len(questionList)):
    current = questionList[i].split('! ')
    for x in range(len(current)-1):
        current[x] = current[x] + '!'
    for x in range(len(current)):
        shoutList.append(current[x])
print(shoutList)
