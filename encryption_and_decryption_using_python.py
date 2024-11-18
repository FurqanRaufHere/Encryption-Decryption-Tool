# Encoding and Decoding using Python 

import random 
import string

def generate_random_chars(n=3):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(n))

def encode(word):
    if (len(word) >= 3):
        word = word[1:] + word[0]
        prefix = generate_random_chars(3)
        suffix = generate_random_chars(3)
        insert_random_char = generate_random_chars(1)
        insert_at_position = random.randint(1, len(word)-1)
        encoded_word = word[:insert_at_position] + insert_random_char + word[insert_at_position:]
        return prefix + encoded_word + suffix
    else:
        return word[::-1]
    
def decode(word):
    if len(word) >= 9:
        word = word[3:-3]

        for i in range(1, len(word), -1):
            if not word[i].isalnum():
                word = word[:i] + word[i+1:]
                break

        decoded_word = word[-1]+ word[:-1]
        return decoded_word
    else:
        return word[::-1]

def processing_message(text_message, mode):
    words = text_message.split()
    if mode == 'encode':
        return ' '.join([encode(word) for word in words])
    elif mode == 'decode':
        return ' '.join([decode(word) for word in words])
    else:
        return "Invalid selection"

def main():
    mode = input("\nWhat do you want to select: 'encode' or 'decode'? ")
    message = input("Enter your message: ")

    if mode in ['encode', 'decode']:
        Result= processing_message(message, mode)
        print(f"Result is: {Result}\n")
    else:
        print("Invalid selection of mode. Kindly select either 'encode' or 'decode' ")

if __name__ == "__main__":
    main()
