import copy

import pkg_resources


class LZW:

    def __init__(self):
        self.base_table = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnipqrstuvwxyz ,.!?;:')
        return

    def Encode(self, msg: str, in_bin_format = False):
        table = copy.copy(self.base_table)
        line = msg[0]
        code = []
        for i in range(1,len(msg)):
            c = msg[i]
            if line+c in table:
                line = line+c
            else:
                code.append(table.index(line))
                table.append(line+c)
                line = c
        code.append(table.index(line))

        if in_bin_format:
            return [bin(c)[2:] for c in code], table

        return code, table

    def Decode(self, code):
        decode_table = copy.copy(self.base_table)
        res = []
        old_code = code[0]
        res.append(decode_table[old_code])
        old_symb = decode_table[old_code]
        for i in range(1,len(code)):
            new_code = code[i]
            line = decode_table[new_code]
            res.append(line)
            symb = line[0]
            decode_table.append(old_symb+symb)
            old_code = new_code
            old_symb = decode_table[new_code]

        return res



msg ="WED WE WEE WEB WET"
print(msg)
c = LZW()
code, t  = c.Encode(msg, in_bin_format=False)
print(code,'\n',t)
msg = c.Decode(code)
print(''.join(msg))