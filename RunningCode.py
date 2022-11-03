from Huffman import *

class RunningCode:
    def __init__(self, use_huffman = True):
        self.flagByte =255
        self._IsHuffmanOn = use_huffman
        if use_huffman:
            self.HuffmanCoder = HuffmanCode()

    def Encode(self, msg, as_list = True):
        '''Закодировть сообщение. Если используется код Хамффмана - будет применяться сначала он'''
        if self._IsHuffmanOn:
            msg = self.HuffmanCoder.Encode(msg, as_list=True)

        stats = self._run(msg)
        code = self._make_code_from_stat(stats)
        if not as_list:
            return ''.join(code)
        return code

    def Decode(self, msg: list, hummfan_code_table = None):
        '''Декодировать сообщение. Если использовался код Хаффмана - нужно вложить словарь соответсвий'''
        res = []
        i=0
        while i <len(msg):
            if msg[i]==bin(self.flagByte)[2:]:
                cnt = int(msg[i+1], base = 2)
                res.extend([msg[i-1]]*(cnt-1))
                i+=2
            else:
                res.append(msg[i])
                i+=1


        if hummfan_code_table is not None:
            r = ''.join(res)
            r = self.HuffmanCoder.Decode(r,hummfan_code_table)
            return r

        return ''.join([chr(int(x, base=2)) for x in res])


    def _run(self, msg):
        prev = msg[0]
        counter = 1
        res = []
        for i in range(1,len(msg)+1):
            if i == len(msg) or msg[i] != msg[i-1]:
                res.append((msg[i-1], counter))
                counter=1
                continue
            counter+=1
        return res

    def _make_code_from_stat(self, stat):
        res = []
        for elem in stat:
            symb =  elem[0] if self._IsHuffmanOn else bin(ord(elem[0]))[2:]
            if elem[1] >=3:
                res.append(symb)
                res.append(bin(self.flagByte)[2:])
                res.append(bin(elem[1])[2:])
            else:
                for i in range(elem[1]):
                    res.append(symb)
        return res





'''bad = ''.join([bin(ord(s))[2:] for s in 'hello world'])
print(bad)
'''

msg = 'aaaaaaaaaaaaaaa Helllllllo woooooooorlddddd'
msg_bin = [bin(ord(symb))[2:] for symb in msg]
print(msg)
print(''.join(msg_bin))
print('----------')


r = RunningCode(use_huffman=False)
s = r.Encode(msg, as_list=True)
print(''.join(s))
dec = r.Decode(s)
print(dec)

print('----------')

r =  RunningCode(use_huffman= True)
s = r.Encode(msg, as_list=True)
code_table = r.HuffmanCoder.GetCodeTable()
print(''.join(s))
dec = r.Decode(s,code_table)
print(dec)




