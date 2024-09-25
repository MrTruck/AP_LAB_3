to_morse= { 'A':'.-',     'B':'-...','C':'-.-.',   'D':'-..','E':'.', 'F':'..-.',   'G':'--.',     'H':'....',

                    'I':'..',     'J':'.---',    'K':'-.-',

                    'L':'.-..',   'M':'--',      'N':'-.',

                    'O':'---',    'P':'.--.',    'Q':'--.-',

                    'R':'.-.',    'S':'...',     'T':'-',

                    'U':'..-',    'V':'...-',    'W':'.--',

                    'X':'-..-',   'Y':'-.--',    'Z':'--..',

                    '1':'.----',  '2':'..---',   '3':'...--',

                    '4':'....-',  '5':'.....',   '6':'-....',

                    '7':'--...',  '8':'---..',   '9':'----.',

                    '0':'-----',  ', ':'--..--', '.':'.-.-.-',

                    '?':'..--..', '/':'-..-.',   '-':'-....-',

                    '(':'-.--.',  ')':'-.--.-', '':'/'}



to_text = {

    '.-':'A',     '-...':'B',   '-.-.':'C',   '-..':'D',

    '.':'E',      '..-.':'F',   '--.':'G',     '....':'H',

    '..':'I',     '.---':'J',   '-.-':'K',     '.-..':'L',

    '--':'M',     '-.':'N',     '---':'O',     '.--.':'P',

    '--.-':'Q',   '.-.':'R',    "...":'S',     '-':'T',

    '..-':'U',    "...-":'V',   '.--':'W',     '-..-':'X',

    '-.--':'Y',   '--..':'Z',   '.----':'1',   '..---':'2',

    "...--":'3',  "....-":'4',  ".....":'5',   "-....":'6',

    "--...":'7',  "---..":'8',  "----.":'9',   "-----":'0',

    "--..--":", ", ".-.-.-":'.',"..--..":'?',  "-..-.":'/',

    "-....-":'-',"-.--.":'(',  "-.--.-":')',"/":' '

}

while True:

    user = input("""To translate TEXT to MORSE CODE type 1,
To translate MORSE CODE to TEXT type 2:
""")

    if user == '1':

        words = input('Enter TEXT:').upper()

        result = ''

        for char in words:

            result += to_morse[char.strip()] + " "

        print(result)



    elif user == '2':

        words = input('Enter MORSE CODE (be sure to add space between letters and "/" between words):')

        result =''

        morse_char = words.split()

        for char in morse_char:

            result += to_text[char]

        print(result)

    else:
        print("Invalid")

    idiot_proofing = input("Would you like to try again? (yes/no): ")
    if idiot_proofing.lower() != 'yes':
        print("Goodbye :)")
        break