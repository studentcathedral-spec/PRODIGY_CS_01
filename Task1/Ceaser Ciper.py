def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():

            # Check uppercase letters
            if char.isupper():
                new_char = chr((ord(char) - 65 + shift) % 26 + 65)

            # Check lowercase letters
            else:
                new_char = chr((ord(char) - 97 + shift) % 26 + 97)

            result += new_char

        else:
            # Keep spaces and symbols unchanged
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# User Input
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

# Encrypt
encrypted = encrypt(message, shift)
print("\nEncrypted Message:", encrypted)

# Decrypt
decrypted = decrypt(encrypted, shift)
print("Decrypted Message:", decrypted)