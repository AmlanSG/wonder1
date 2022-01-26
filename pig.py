s = 'Jingle bells, jingle bells!\nJingle all the way!!\nOh, what fun it is to ride\nIn a one horse open sleigh.'

def capitalizeFirstWord(word):
    return word[0].upper() + word[1:]               # genearates word starting with a capital letter

def generatePigWord(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word[0] in vowels:                           # if the first letter in a word is a vowel
        return(word + 'way')                        # return pig_latin word
    
    # if the first letter in a word is not a vowel
    suffix_word = ''
    prefix_word = word
    for i in range(len(word)):
        if word[i] in vowels:
            break
        suffix_word += word[i]
        prefix_word = word[i+1:]
    return(prefix_word + suffix_word + 'ay')        # return pig_latin word

def pig_latin(s):
    translation = ''                                # To generate final pig_latin sentence
    for sentence in s.split('\n'):                  # splitting corpus to list of sentences
        bag_of_words = sentence.lower().split(' ')  # Listing the words in a sentence
        
        first_word_flag = True
        
        pig_sentence = ''
        for word in bag_of_words:
            pig_word = None
            if word.isalpha():                      # check if the word has special charaters
                pig_word = generatePigWord(word)
            else:
                words_and_spl_characters = None
                for i in range(len(word)):          # listing words and special characters
                    if not word[i].isalpha():
                        words_and_spl_characters = [word[:i],word[i:]]
                        break  
                pig_word = generatePigWord(words_and_spl_characters[0]) + words_and_spl_characters[1]
                
            if(first_word_flag):
                first_word_flag = False
                pig_word = capitalizeFirstWord(pig_word)    #Capitalizing first letter of the sentence
            pig_sentence += pig_word + ' '
        translation +=  pig_sentence + '\n'
    return translation

print(pig_latin(s))


    
    
    
    