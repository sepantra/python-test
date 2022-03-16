array = ['\n']
isLoop = True
while isLoop :
    words= input('Type any words to sort them in an alphabetical order,to see the results please write "cancel" : ')
    if words != 'cancel':
        array.append(words)
    elif words == 'cancel' : isLoop = False
print(*sorted(array), sep = '\n')