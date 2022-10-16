def caesar(message: str) -> None:

    """
    Encodes a message using the caesar cypher
    Input:
      message: string
    Output:
    encoded_string: string

    """

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shift = 3
    encoded_string = ""

    for letter in message:
        if letter not in alphabet:
            encoded_string += letter
        if letter in alphabet:
            new_letter = ord(letter) + shift
            if new_letter > ord(alphabet[-1]):
                new_letter_start = (new_letter - ord(alphabet[-1])) + ord(alphabet[0])
                encoded_string += chr(new_letter_start)
            if new_letter < ord(alphabet[-1]):
                encoded_string += chr(new_letter)
    return encoded_string