import random

def main():
    while True:
        first_name = input("Enter your first name (you can leave blank or type quit to exit): ").strip()
        if first_name.lower() == "quit":
            print("Goodbye! Have a spooky day!")
            break
        last_name = input("Enter your last name (you can leave blank or type quit to exit): ").strip()
        if last_name.lower() == "quit":
            print("Goodbye! Have a spooky day!")
            break
        
        spooky_first_name, spooky_last_name = generate_spooky_name(first_name, last_name)

        print(f"Your spooky name is: {spooky_first_name} {spooky_last_name}")

def generate_spooky_name(first_name="", last_name=""):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    spooky_first_name = ""
    spooky_last_name = ""

    if first_name:
        for letter in first_name.lower():
            if letter in vowels:
                spooky_first_name += random.choice(vowels)
            elif letter in consonants:
                spooky_first_name += random.choice(consonants)
            else:
                spooky_first_name += letter
    else:
        spooky_first_name = first_name  # Assign the original first name if it's empty

    if last_name:
        for letter in last_name.lower():
            if letter in vowels:
                spooky_last_name += random.choice(vowels)
            elif letter in consonants:
                spooky_last_name += random.choice(consonants)
            else:
                spooky_last_name += letter
    else:
        spooky_last_name = last_name  # Assign the original last name if it's empty

    return spooky_first_name.capitalize(), spooky_last_name.capitalize()

if __name__ == "__main__":
    main()
