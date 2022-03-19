outputWords = ['\n']
isLoop = True
while isLoop :
    inputWord = input('Type any words to sort them in an alphabetical order,to see the results please write "cancel" : ')
    if inputWord != 'cancel':
        outputWords.append(inputWord)
    elif inputWord == 'cancel' : 
        isLoop = False
print(*sorted(outputWords), sep = '\n')