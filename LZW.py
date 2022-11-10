import copy

import pkg_resources


class LZW:

    def __init__(self):
        self.base_table = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmniopqrstuvwxyz ,.!?;:\n')
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
        prev_code = code[0]
        prev_line = decode_table[prev_code]
        res.append(prev_line)
        for i in range(1,len(code)):
            current_code = code[i]
            if current_code >= len(decode_table):
                line = prev_line+prev_line[0]
            else:
                line = decode_table[current_code]
            res.append(line)
            decode_table.append(prev_line+line[0])
            #prev_symb = decode_table[current_code]
            prev_line = line


        return res

    def __str__(self):
        return 'LZW код'

'''
msg ="WED WE WEE WEB WET"
print(msg)
c = LZW()
code, t  = c.Encode(msg, in_bin_format=False)
print(code,'\n',t)
msg = c.Decode(code)
print(''.join(msg))'''