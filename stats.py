def get_words_count(filecontent):
    list = filecontent.split()
    return len(list)

def get_letters_count(filecontent):
    filecontent = filecontent.lower()
    dict = {}

    for char in filecontent:
        if char not in dict:
            dict.update({char: 1})
        else:
            dict[char] +=  1

    return dict
