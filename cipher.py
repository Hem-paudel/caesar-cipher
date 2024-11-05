# add your code here
def caesar_cipher(text, shift=5):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - offset + shift) % 26 + offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
            
    return encrypted_text

plain_text = input("Please enter a sentence: ")
encrypted_text = caesar_cipher(plain_text)
print("The encrypted sentence is:", encrypted_text)
