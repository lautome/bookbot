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

def get_ordered_letters(dict):
    # Keep alpha chars in a new dictionary
    new_dict = {}
    for d in dict:
        if d.isalpha():
            new_dict.update({d: dict[d]})

    # Split new_dict's data as requested
    list_of_dictionaries = []
    for nd in new_dict:
        x = {"char": nd, "num": new_dict[nd]}
        list_of_dictionaries.append(x)

    # sort() is keyword-only, thus get_value() is needed
    list_of_dictionaries.sort(key=get_value, reverse=True)

    for lod in list_of_dictionaries:
        print(f"{lod["char"]}: {lod["num"]}")

# Needed for sort() in get_ordered_letters
def get_value(dict):
    return dict["num"]
