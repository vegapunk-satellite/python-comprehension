read_log_file = (r'"C:/Users/Asus/PycharmProjects/newproject/to-do.txt"', 'to-do.txt:')

def read_log_file(filename, keyword):   #file

    saved_word = []  # Array
# read file
    with open(filename) as file_search:   #open search file
        file_search = file_search.readlines()   #read file
    for lines in file_search:    # every word is scaned
           if keyword in lines:   # extract the keyword
                saved_word.append(lines)    #store all found keywords in array
        # write in new file
    with open('to-do.txt', 'a+') as file_handler:
        file_handler.write(f"{filename}\n")
        for i in range(len(saved_word)):
            file_handler.write(f"{saved_word[i]}")

    print('done') # completed

    print(len(saved_word)) # count found words



