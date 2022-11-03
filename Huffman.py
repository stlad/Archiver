import  copy

class HuffmanCode:
    def __init__(self):
        self.frequencies = {}
        self.code_table = {}

    def Decode(self, msg, code_table):
        code_to_symb = ReverseDct(code_table)
        words = list(code_to_symb.keys())
        decoded_msg = ''
        buffer = ''
        for s in msg:
            buffer+=s
            if words.__contains__(buffer):
                decoded_msg += code_to_symb[buffer]
                buffer = ''

        return decoded_msg

    def Encode(self,msg , as_list = False):
        self._create_code(msg)
        res=[]
        for symb in msg:
            res.append(self.code_table[symb])

        if as_list:
            return res
        return ''.join(res)

    def EncodeAsASCIItext(self, msg):
        codedMsg = self.Encode(msg, True)
        res = []
        for sym in codedMsg:
            res.append(chr(int(sym, base=2)))
        return ''.join(res)


    def GetCodeTable(self):
        return self.code_table



    def _create_code(self, text):
        self.frequencies = self._count_frequensies(text)
        self.tree = self._create_tree()
        self.tree.Traverse(self.code_table,'')

    def _count_frequensies(self, text):
        symbols = set(text) # получаем список символов в тексте
        res = [(symb,  text.count(symb)) for symb in symbols ] # находим количество каждого символа в тексте
        res.sort(key = lambda x: (x[1], x[0]), reverse=False ) # сортируем по возрастанию частот
        return res

    def _create_tree(self):
        tree = copy.copy(self.frequencies)
        tree = [HuffmanTreeNode(value= leave[1], str_val=leave[0]) for leave in tree]

        while len(tree) >1:
            #new_node = [(tree[0][0]+tree[1][0], tree[0][1] + tree[1][1])]
            #new_tree_node = HuffmanTreeNode()
            new_node = tree[0] + tree[1]
            tree = [new_node] + tree[2:]
            tree.sort(key = lambda x: x.Value, reverse=False )
        return tree[0]



class HuffmanTreeNode:
    def __init__(self,root = None, left = None, right = None, value=0, str_val = ''):
        self.Left = left
        self.Right = right
        self.Root = root
        self.Value = value
        self.StringValue = str_val

    def __add__(self, other):
        new_node=HuffmanTreeNode(
            left=self,
            right=other,
            value=self.Value+other.Value,
            str_val= self.StringValue + other.StringValue
        )
        self.Root = new_node
        other.Root = new_node
        return new_node

    def Traverse(self, res_dct, current_way):
        if self.Left is None and self.Right is None:
            if self.Root is None:
                current_way = '0'
            res_dct[self.StringValue] = current_way
            return

        self.Left.Traverse(res_dct, current_way+'0')
        self.Right.Traverse(res_dct, current_way+'1')
        pass


def ReverseDct(dct):
    new_dct = {}
    for index,key in enumerate(dct):
        new_key = dct[key]
        new_val = key
        new_dct[new_key] = new_val
    return new_dct



'''msg = "hello world"
bad = ''.join([bin(ord(s))[2:] for s in msg])
print(bad)

h =HuffmanCode()
code = h.Encode(msg)
print(code)
code_table = h.GetCodeTable()
print(h.Decode(code, code_table))
#decoder = HuffmanCode()
#res = decoder.Decode(code, code_table)
#print(res)
'''


