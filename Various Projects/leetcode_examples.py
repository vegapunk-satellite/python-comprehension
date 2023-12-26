# Program to sort alphabetically the words form a string provided by the user
#
# my_str = input("Enter some words to sort them out alphabetically: ")
#
# words = [word.lower() for word in my_str.split()]
#
# words.sort()
#
# print("The sorted words are:")
# for word in words:
#    print(word)

#  Function to print binary number using recursion
# def convertToBinary(n):
#    if n > 1:
#        convertToBinary(n//2)
#    print(n % 2,end = '')
#
# dec = int(input("Please type in a decimal integer for binary coversion: "))
#
# convertToBinary(dec)
# print()

# Program to add two matrices

#
# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
#
# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]
#
# result = [[0,0,0],
#          [0,0,0],
#          [0,0,0]]
#
# for i in range(len(X)):
#    for j in range(len(X[0])):
#        result[i][j] = X[i][j] + Y[i][j]
#
# for r in result:
#    print(r)

# def convert_to_english(turkish_string):
#     differing_characters = {"ğ": "g", "ö": "o", "ü": "u", "ş": "s", "ç": "c", "İ": "I", "ı": "i"}
#     new_string = ""
#     for char in turkish_string:
#         if char in differing_characters:
#             new_string += differing_characters[char]
#         elif char.lower() in differing_characters:
#             new_string += differing_characters[char.lower()].upper()
#         else:
#             new_string += char
#     return new_string
#
# turkish_string = "Benim öğretmenimin İŞ Bankası'nda hesabı var."
# english_string = convert_to_english(turkish_string)
# print(f"Turkish string is {turkish_string} and converted string is {english_string}")

# Convert a 4-digit number from integer to text form

#2345

def convert_to_text(number):
    integer_to_string_digit_1 = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    # integer_to_string_digit_2 = {10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
    #         15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen",
    #         20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy",
    #         80: "Eighty", 90: "Ninety"}

    integer_to_string_digit_2 = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty",
                                 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}

    def ones_conversion(char):
        return integer_to_string_digit_1[char]

    def tens_conversion(char):
        return integer_to_string_digit_2[char]

    def hundreds_conversion(char):
        return integer_to_string_digit_1[char] + " Hundred"

    def thousands_conversion(char):
        return integer_to_string_digit_1[char] + " Thousand"

    def ten_thousands_conversion(char):
        return integer_to_string_digit_2[char] + " Thousand"

    def thousands_conversion(char):
        return integer_to_string_digit_1[char] + " Thousand"

    conversion_functions = [ones_conversion, tens_conversion, hundreds_conversion, thousands_conversion, ten_thousands_conversion]

    output = ""
    number_string = str(number)
    function_index = 0
    for char in reversed(number_string):
        output = conversion_functions[function_index](int(char)) + " " + output
        function_index += 1
    return output

print(convert_to_text(23456))

# hex to rgb color converter