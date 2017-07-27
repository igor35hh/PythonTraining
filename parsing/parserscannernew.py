from _ast import Num

TraceDefault = False

class UndefinedError(Exception):
    pass

from parsing.scanner import Scanner, LexicalError, SyntaxError

class TreeNode:
    def validate(self, dict):
        pass
    def apply(self, dict):
        pass
    def trace(self, level):
        print('.' * level + '<empty>')
        
class BinaryNode(TreeNode):
    def __init__(self, left, right):
        self.left, self.right = left, right
    def validate(self, dict):
        self.left.validate(dict)
        self.right.validate(dict)
    def trace(self, level):
        print('.' * level + '[' + self.label + ']')
        self.left.trace(level+3)
        self.right.trace(level+3)
        
class TimesNode(BinaryNode):
    label = '*'
    def apply(self, dict):
        return self.left.apply(dict) * self.right.apply(dict)
    
class DivideNode(BinaryNode):
    label = '/'
    def apply(self, dict):
        return self.left.apply(dict) / self.right.apply(dict)
    
class PlusNode(BinaryNode):
    label = '+'
    def apply(self, dict):
        return self.left.apply(dict) + self.right.apply(dict)
    
class MinusNode(BinaryNode):
    label = '-'
    def apply(self, dict):
        return self.left.apply(dict) - self.right.apply(dict)
    
class NumNode(TreeNode):
    def __init__(self, num):
        self.num = num
    def apply(self, dict):
        return self.num
    def trace(self, level):
        print('.' * level + repr(self.num))
        
class VarNode(TreeNode):
    def __init__(self, text, start):
        self.name = text
        self.column = start
    def validate(self, dict):
        if not self.name in dict.keys():
            raise UndefinedError(self.name, self.column)
    def apply(self, dict):
        return dict[self.name]
    def assign(self, value, dict):
        dict[self.name] = value
    def trace(self, level):
        print('.' * level + self.name)
        
class AssignNode(TreeNode):
    def __init__(self, var, val):
        self.var, self.val = var, val
    def validate(self, dict):
        self.val.validate(dict)
    def apply(self, dict):
        self.var.assign(self.val.apply(dict), dict)
    def trace(self, level):
        print('.' * level + 'set')
        self.var.trace(level+3)
        self.var.trace(level+3)
        
class Parser:
    def __init__(self, text=''):
        self.lex = Scanner(text)
        self.vars = {'pi': 3.14159}
        self.traceme = TraceDefault
        
    def parse(self, *text):
        if text:
            self.lex.newtext(text[0])
        tree = self.analyse()
        if tree:
            if self.traceme:
                print(); tree.trace(0)
            if self.errorCheck(tree):
                self.interpret(tree)
                
    def analyse(self):
        try:
            self.lex.scan()
            return self.Goal()
        except SyntaxError:
            print('Syntax error at column:', self.lex.start)
            self.lex.showerror()
        except LexicalError:
            print('Lexical error at column:', self.lex.start)
            self.lex.showerror()
            
    def errorCheck(self, tree):
        try:
            tree.validate(self.vars)
            return 'ok'
        except UndefinedError as instance:
            varinfo = instance.args
            print("'%s' is underfined at column: %d" % varinfo)
            self.lex.start = varinfo[1]
            self.lex.showerror()
            
    def interpret(self, tree):
        result = tree.apply(self.vars)
        if result != None:
            print(result)
            
    def Goal(self):
        if self.lex.token in ['num', 'var', '(']:
            val = self.Expr()
            self.lex.match('\0')
            return val
        elif self.lex.token == 'set':
            val = self.Assign()
            self.lex.match('\0')
            return val
        else:
            raise SyntaxError()
        
    def Assign(self):
        self.lex.match('set')
        var = VarNode(self.lex.value, self.lex.start)
        self.lex.match('var')
        val = self.Expr()
        return AssignNode(var, val)
        
    def Expr(self):
        left = self.Factor()
        while True:
            if self.lex.token in ['\0', ')']:
                return left
            elif self.lex.token == '+':
                self.lex.scan()
                left = PlusNode(left, self.Factor())
            elif self.lex.token == '-':
                self.lex.scan()
                left = MinusNode(left, self.Factor())
            else:
                raise SyntaxError()
        
    def Factor(self):
        left = self.Term()
        while True:
            if self.lex.token in ['+', '-', '\0', ')']:
                return left
            elif self.lex.token == '*':
                self.lex.scan()
                left = TimesNode(left, self.Term())
            elif self.lex.token == '/':
                self.lex.scan()
                left = DivideNode(left, self.Term())
            else:
                raise SyntaxError()
            
    def Term(self):
        if self.lex.token == 'num':
            val = NumNode(self.lex.match('num'))
            return val
        elif self.lex.token == 'var':
            val = VarNode(self.lex.value, self.lex.start)
            self.lex.scan()
            return val
        elif self.lex.token == '(':
            self.lex.scan()
            val = self.Expr()
            self.lex.match(')')
            return val
        else:
            raise SyntaxError()

if __name__ == '__main__':
    x = Parser('4 / 2 + 3')
    x.parse()
    x.parse('4.0 / 2 * 3')
    x.parse('(4.0 / 2) * 3')
    x.parse('4.0 / (2 * 3)')
    x.parse('(((3))) + 1') 
    print('***')
    z = Parser()
    z.parse('set a 99')
    z.parse('set a a + 1')
    z.parse('a')   
    print('***')
    z = Parser()
    z.parse('pi')
    z.parse('2 * pi')
    z.parse('1.234 + 2.1')        
            
