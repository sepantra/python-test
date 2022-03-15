array = ['\n']
while True :
    words= input('Write any words to sort them in an alphabetical order,to see the results please write "cancel" : ')
    if words != 'cancel':
        array.append(words)
    elif words == 'cancel' : break
print(*sorted(array), sep = '\n')