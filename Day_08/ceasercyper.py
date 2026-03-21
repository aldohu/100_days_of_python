def code_word(word, number):
    """Encodes or decodes a word based on shift number"""
    word = word.lower()
    cyphered_word = ""
    for char in word:
        if char.isalpha():
            shifted = ord(char) + number
            if shifted > ord('z'):
                shifted -= 26
            elif shifted < ord('a'):
                shifted += 26
            cyphered_word += chr(shifted)
        else:
            cyphered_word += char
    return cyphered_word

# Main program
last_encoded_word = ""
last_shift_number = 0
has_encoded_word = False

while True:
    print("\n" + "="*40)
    cyper = input("Options:\n- Encode (e)\n- Decode (d)\n- Exit (exit)\n\nYour choice: ")
    
    if cyper.lower() == 'exit':
        print("\nGoodbye! Thanks for using the cipher program.")
        break
    
    if cyper.lower() == 'e' or cyper.lower() == "encode":
        # Get word and number from user
        word = input("Enter a word to encrypt: ")
        number = int(input("Enter a number to shift by: "))
        
        # Encode the word and save it
        last_encoded_word = code_word(word, number)
        last_shift_number = number
        has_encoded_word = True
        
        print(f"\n✓ Original word: {word}")
        print(f"✓ Encoded word: {last_encoded_word}")
        print(f"✓ Shift used: {number}")
        
    elif cyper.lower() == 'd' or cyper.lower() == "decode":
        # FIRST check if there's an encoded word available
        if not has_encoded_word:
            print("\n⚠ ERROR: No word has been encoded yet!")
            print("Please encode a word first before trying to decode.")
            continue  # Skip the rest and go back to menu
        
        # Only ask for decode option if there's an encoded word
        print(f"\nCurrent encoded word: {last_encoded_word}")
        decode_choice = input("Do you want to decode this word? (y/n): ")
        
        if decode_choice.lower() == 'y' or decode_choice.lower() == 'yes':
            # Decode the last encoded word
            decoded_word = code_word(last_encoded_word, -last_shift_number)
            print(f"\n✓ Encoded word: {last_encoded_word}")
            print(f"✓ Decoded word: {decoded_word}")
            print(f"✓ Shift used: {last_shift_number}")
        else:
            print("\nDecode cancelled. Returning to main menu.")
    
    else:
        print("\n⚠ Invalid option. Please enter 'e' for encode, 'd' for decode, or 'exit' to quit.")