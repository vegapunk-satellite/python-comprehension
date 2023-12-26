MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


MORSE_CODE_DICT_REVERSED = { value: key for (key,value) in MORSE_CODE_DICT.items() }
print(MORSE_CODE_DICT_REVERSED)

class MorseCode:

    def encode(self, message):
        encoded_message = ""
        for char in message:
            if char == " ":
                encoded_message += "/ "
            else:
                encoded_message += MORSE_CODE_DICT[char.upper()] + " "
        return encoded_message

    def decode(self, encoded_message):
        decoded_message = ""
        encoded_message_parts = encoded_message.split(" ")
        print("Encoded message parts: " + str(encoded_message_parts))
        for part in encoded_message_parts:
            if part == "":
                continue
            elif part == "/":
                decoded_message += " "
            else:
                decoded_message += MORSE_CODE_DICT_REVERSED[part]
        return decoded_message



message = input("Enter your message: ")
morse_code = MorseCode()

encoded_message = morse_code.encode(message)
print(f"Encoded message =  <{encoded_message}>")

decoded_message = morse_code.decode(encoded_message)
print(f"Decoded message = <{decoded_message}>")


