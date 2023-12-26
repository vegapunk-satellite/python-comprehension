def convertSnakeCaseToPascalCase(input_string):
    words = input_string.split("_")
    output_string = ""
    for word in words:
        output_string += word[0].upper() + word[1:]
    return output_string


test = "i_love_birds"
print(convertSnakeCaseToPascalCase(test)) # ILoveBirds

test = "some_interesting_book_title"
print(convertSnakeCaseToPascalCase(test)) # SomeInterestingBookTitle

