from Huffman import *
from LZW import *
from RunningCode import *
from utilits import *


def OriginalTextInfo(text):
    print('----------------------------------')
    print(f'оригинальный текст: \n{text}')
    binary_original_text = TextToBin(text)
    print(f'двоичный вид:\n{binary_original_text}')
    print(f'Длина: {len(binary_original_text)} бит')


def HuffmanInfo(text):
    print('----------------------------------')
    print('КОД ХАФФМАНА')
    h = HuffmanCode()
    code = h.Encode(text)
    table = h.GetCodeTable()
    print(f'Закодированный текст:\n{code}')
    print(f'Таблица кодовых слов:{table}')
    print(f'Длина: {len(code)} бит')
    decoded_msg = h.Decode(code, table)
    print(f'Декодированный текст:\n{decoded_msg}')


def RunningWithHuffMan(text):
    print('----------------------------------')
    print('RUNNING CODE с Кодом Хаффмана')
    r = RunningCode(use_huffman=True)
    code = r.Encode(text, as_list=True)
    str_code = ''.join(code)
    print(f'Закодированное сообщение:\n{str_code}')
    print(f'Длина: {len(str_code)} бит')
    code_table = r.HuffmanCoder.GetCodeTable()
    print(f'Таблица для кода Хаффмана: {code_table}')
    decoded_msg = r.Decode(code,code_table)
    print(f'Декодированный текст:\n{decoded_msg}')
    pass

def RunningOnly(text):
    print('----------------------------------')
    print('RUNNING CODE')
    r = RunningCode(use_huffman=False)
    code = r.Encode(text, as_list=True)
    str_code = ''.join(code)
    print(f'Закодированное сообщение:\n{str_code}')
    print(f'Длина: {len(str_code)} бит')
    decoded_msg = r.Decode(code)
    print(f'Декодированный текст:\n{decoded_msg}')


def LZWInfo(text):
    print('----------------------------------')
    print('LZW CODE')
    lzw = LZW()
    code, t  = lzw.Encode(text, in_bin_format=False)
    decoded_msg = lzw.Decode(code)
    print(f'Закодированное сообщение:\n{code}')
    bin_code = ''.join([bin(c)[2:] for c in code])
    print(f'Кодовая таблица: \n{t}')
    print(f'Закодированное сообщение в двоичном формате\n{bin_code}')
    print(f'Длина: {len(bin_code)} бит')
    print(f'Декодированный текст:\n{"".join(decoded_msg)}')

with open('texts/6.txt', 'r', encoding='utf-8') as file:
    text = file.read()


OriginalTextInfo(text)
HuffmanInfo(text)
RunningOnly(text)
RunningWithHuffMan(text)
LZWInfo(text)
