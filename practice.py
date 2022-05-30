def p_test(name):
    """ Prints out values"""
    return (f"Hello {name}, welcome")
hello = p_test("Flint")
print(hello)

def word_count():
    """ Takes a text document and returns a dictionary of words and their counts """
    words = {}
    file_name = input("Please input file name or path:  ")
    with open(file_name,"r") as text_file:
        text = text_file.read()
        f_text = text.split()
        #print(f_text)
        for word in f_text:
            if word not in words:
                words[word]= 1
            else:
                words[word] = words[word] + 1
    return words

print (word_count())