def challange1():
    height = int(input("whats the height"))
    length = int(input("wahts the length"))
    trigArea = (height * length / 2)
    print (trigArea)

   
def challange3(num, numm):
    num = int(num)
    numm = int(numm)

 

    if num % 7 == 0 or numm % 7 == 0:
        print(num / numm)
    elif num % 11 == 0 or numm % 11 == 0:
        print( num * numm)

    print(num + numm)



def challange4():
    years = int(input("what years is it"))
    days = years*365
    print (days)


challange3(7, 11)

def challange5(morse):
    morseCode = ""
    morse = morse.upper()

    char_to_dots = {
      'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
      'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
      'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
      'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
      'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
      '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
      '6': '-....', '7': '--...', '8': '---..', '9': '----.',
      '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
      ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
      '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
    }

    for i in morse:
        morseCode += char_to_dots[i]

    return morseCode
    
print(challange5("Alex"))
    
