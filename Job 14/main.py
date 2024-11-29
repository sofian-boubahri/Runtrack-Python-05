def my_long_word(n, sentence):
    words = []
    
    word = ""
    
    for char in sentence:
        if char != ' ':
            word += char
        else:
            if len(word) > n:
                words.append(word)
            word = ""  
            
    if len(word) > n:
        words.append(word)
    
    result = ""
    for w in words:
        result += w + " "
    
    return result.strip() 
sentence = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
print(my_long_word(3, sentence))
