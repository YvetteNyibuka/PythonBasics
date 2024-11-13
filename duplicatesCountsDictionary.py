def word_indices(s):
    words = s.split() 
    index_dict = {}  
    
    for index, word in enumerate(words):
        if word in index_dict:
            index_dict[word].append(index)
        else:
            index_dict[word] = [index]
    
    return index_dict

text = "this is a test this is only a test"
print(word_indices(text))
