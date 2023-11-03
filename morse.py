# Dicctionary to convert text to morse code
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'
}
# Reverse the dictionary for decoding Morse code to text
reverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}

def main():
    while True:
        print("What do you want to convert?")
        print("1. Morse Code to Text (Type '1')")
        print("2. Text to Morse Code (Type '2')")
        print("Type 'quit' to exit the program.")
        
        # Get user input for the conversion choice
        choice = input("Select one option: ")
        
        # Check user choice and perform the corresponding conversion
        if choice.lower() == "quit":
            print("Goodbye!")  # Exit the program if the user types 'quit'
            break
        elif choice == '1':
            morse_code = input("Enter the Morse Code to be converted to text: ")
            result = morse_code_to_text(morse_code)
            print(f"Text for the code '{morse_code}' is: {result}")
        elif choice == '2':
            text = input("Enter the text to be converted to Morse Code: ")
            result2 = text_to_morse(text)
            print(f"Morse Code for '{text}' is: {result2}")
        else:
            print("Invalid choice. Please choose a valid option.")  # Handle invalid user input

def morse_code_to_text(morse_code):
    morse_code_words = morse_code.split(' ')
    text = []
    for word in morse_code_words:
        if word in reverse_morse_code_dict:
            text.append(reverse_morse_code_dict[word])
        else:
            text.append(word)  # Keep non-Morse code characters as they are
    return ''.join(text)
    
def text_to_morse(text):
    morse = []
    for char in text.upper():  # Ensure the input text is converted to uppercase for consistency
        if char in morse_code_dict:
            morse.append(morse_code_dict[char])
        else:
            morse.append(char)  # Keep non-alphabetic characters as they are
    return " ".join(morse)

if __name__ == "__main__":
    main()
 #   - .... . / .-- . . -.- -. -..