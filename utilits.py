def TextToBin(text):
    return ''.join([bin(ord(symb))[2:] for symb in text])