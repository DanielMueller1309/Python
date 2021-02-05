import re
sentence = str(input("Kopieren Sie sich hier ihre Sätze rein:"))
split_sentence = re.split("([!]|[§]|[$]|[%]|[&]|[/]|[(]|[)]|[=]|[?]|[*]|[;]|[:]|[,]|[.]|[+]|[_]|[<]|[>]|)" , sentence)
print(split_sentence)

i = 0


# Schleife um Sonderzeichen zu Separieren
"""
while i in range(len(split_sentence)):                                                                                  # wörterschleife
    for j in range(len(split_sentence[i])):                                                                             # Buchstabenschleife
        if split_sentence[i][j] in ['.', '!', '?', '´', ':']:                                                           # Abfrage welche Satzzeichen gesucht werden sollen
            if j < (len(split_sentence[i]) - 1):                                                                        # wenn zum beispiel nach einem Punkt kein freizeichen gelassen wurde oder ein Apostrof mitten im wort steht
                if j+1 == len(split_sentence[i]) - 1:                                                                   # kommt nach dem Satz/Sonderzeichen nur ein weiterer Buchstabe muss die zweite eckige klammer beim insert an in dieser if angepasst werden
                    if i == len(split_sentence)-1:                                                                      # wenn das ende der liste erreicht ist funktioniert insert nicht
                        split_sentence.append(split_sentence[i][j + 1])
                    else:
                        split_sentence.insert(i + 1, split_sentence[i][j+1])                                            # bei einem Zeichen muss keine range eingerichtet werden
                    split_sentence[i] = split_sentence[i].replace(split_sentence[i][j+1], "")                           # löschung des zeichen nach dem Sonderzeichen
                else:
                    if i == len(split_sentence)-1:
                        split_sentence.append(split_sentence[i][j + 1:len(split_sentence[i]) - 1])
                    else:
                        split_sentence.insert(i + 1, split_sentence[i][j+1:len(split_sentence[i]) - 1])                     # bei mehr als einem zeichen nach dem sonderzeichen muss eine range festgelegt werden
                    split_sentence[i] = split_sentence[i].replace(split_sentence[i][j+1:len(split_sentence[i]) - 1], "")# löschung der zeichen nach dem Sonderzeichen
            split_sentence.insert(i + 1, split_sentence[i][j])                                                          # das sonderzeichen wird an den nächsten listenplatz kopiert
            split_sentence[i] = split_sentence[i].replace(split_sentence[i][j], "")                                     # das sonderzeiche wird am alten Platz gelöscht
            i += 1                                                                                                      # um bei einem erkannten sonderzeichen nicht in eine endlosschleife nach dessen verschiebung zu geraten wird ihr dieses hiermit übersprungen
    i += 1
"""
print(split_sentence)
