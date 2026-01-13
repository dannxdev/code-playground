def caesar(text, shift, encrypt=True):
    # Verifica si shift es un entero
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    # Verifica si shift está entre 1 y 25
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    # Define el alfabeto base en minúsculas
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Invierte el shift para desencriptar si encrypt es False
    if not encrypt:
        shift = - shift

    # Crea el alfabeto desplazado rotando el original
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    # Genera la tabla de traducción para minúsculas y mayúsculas
    translation_table = str.maketrans(
        alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    # Aplica la traducción al texto
    encrypted_text = text.translate(translation_table)
    return encrypted_text


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


my_encrypted_text = "Pbhentr vf sbhaq va hayvxryl cynprf."
decrypted_text = decrypt(my_encrypted_text, 13)
print(decrypted_text)
