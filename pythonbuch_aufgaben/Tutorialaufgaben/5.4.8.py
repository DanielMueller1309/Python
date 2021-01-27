sentence = str(input("Kopieren Sie sich hier ihre Sätze rein:"))
split_sentence = sentence.split()
#s = split_sentence[0].removesuffix(split_sentence[0][len(split_sentence[0])-1])
print(split_sentence)
#print(s)

i = 0
# Schleife um Sonderzeichen zu Separieren
while i in range(len(split_sentence)): # wörterschleife
    for j in range(len(split_sentence[i])): # Buchstabenschleife
        if split_sentence[i][j] in ['.', '!', '?', '´', ':']: # Abfrage welche Satzzeichen gesucht werden sollen
            if j < (len(split_sentence[i]) - 1): #wenn zum beispiel nach einem Punkt kein freizeichen gelassen wurde oder ein Apostrof mitten im wort steht
                if j+1 == len(split_sentence[i]) - 2: #kommt nach dem Satz/Sonderzeichen nur ein weiterer Buchstabe muss die zweite eckige klammer beim insert an in dieser if angepasst werden
                    split_sentence.insert(i + 1, split_sentence[i][j+1]) # bei einem Zeichen muss keine range eingerichtet werden
                else:
                    split_sentence.insert(i + 1, split_sentence[i][j+1:len(split_sentence[i]) - 1]) # bei mehr als einem zeichen nach dem sonderzeichen muss eine range festgelegt werden
            split_sentence.insert(i + 1, split_sentence[i][j]) # das sonderzeichen wird an den nächsten listenplatz kopiert
            split_sentence[i] = split_sentence[i].replace(split_sentence[i][j], "")
            #split_sentence[i] = split_sentence[i].removesuffix(split_sentence[i][len(split_sentence[i])-1])
            i += 1
    i += 1
print(split_sentence)
