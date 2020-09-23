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
                    '(':'-.--.', ')':'-.--.-' }

def text_to_code(message: str) -> str:
    output = '' 
    user_input = message.upper()
    for letter in user_input:
        #print(letter)
        if letter != ' ':
            output += MORSE_CODE_DICT[letter] + ' '
        else:
            output += ' '
    return output

def code_to_text(message: str) -> str:
    print(message)
    user_input = message.split()
    output = ''  # FIX: Converted text is not word spaced
    for char in user_input:
        if char == ' ':
            output += ' '
        else:
            for letter, code in MORSE_CODE_DICT.items():
                if code == char:
                    output += letter
    return output

if __name__ == '__main__':
    message = input("Enter message: ")
    print(code_to_text((text_to_code(message))))
