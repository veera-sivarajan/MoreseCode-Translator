MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', # // represents space between words
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
                    '(':'-.--.', ')':'-.--.-', ' ':'//' }

def text_to_code(message: str) -> str:
    output = '' 
    user_input = message.upper()
    for letter in user_input:
        #print(letter)
        output += MORSE_CODE_DICT[letter] + ' '
    return output

def code_to_text(message: str) -> str:
    user_input = message.split()
    output = ''  
    for char in user_input:
        for letter, code in MORSE_CODE_DICT.items():
            if code == char:
                output += letter
    return output

if __name__ == '__main__':
    message = input("Enter message: ")
    output = (text_to_code(message))
    print(output)
    code = code_to_text(output)
    print(code)
