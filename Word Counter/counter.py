def count(): #Defining the main function
    print ("Welcome to word counter!")
    text = input("Enter your text here: ")
    
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    
    print (f"\n Total words: {word_count}")
    print (f"\n Total characters: {char_count}")
    
if __name__ == "__main__":
    count()