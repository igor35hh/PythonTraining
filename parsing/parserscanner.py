class UndefinedError(Exception):
    pass

from parsing.scanner import Scanner, LexicalError, SyntaxError

class Parser:
    def __init__(self, text=''):
        self.lex = Scanner(text)
        self.vars = {'pi': 3.14159}
        
    def parse(self, *text):
        if text:
            self.lex.newtext(text[0])
        try:
            self.lex.scan()
            self.Goal()
        except SyntaxError:
            print('Syntax Error at column:', self.lex.start)
            self.lex.showerror()
        except LexicalError:
            print('Lexical Error at column:', self.lex.start)
            self.lex.showerror()
        except UndefinedError as E:
            name = E.args[0]
            print("'%s' is underfined at column:" % name, self.lex.start)
            self.lex.showerror()
            
    def Goal(self):
        if self.lex.token in ['num', 'var', '(']:
            val = self.Expr()
            self.lex.match('\0')
            print(val)
        elif self.lex.token == 'set':
            self.Assign()
            self.lex.match('\0')
        else:
            raise SyntaxError()
        
    def Assign(self):
        self.lex.match('set')
        var = self.lex.match('var')
        val = self.Expr()
        self.vars[var] = val
        
    def Expr(self):
        left = self.Factor()
        while True:
            if self.lex.token in ['\0', ')']:
                return left
            elif self.lex.token == '+':
                self.lex.scan()
                left = left + self.Factor()
            elif self.lex.token == '-':
                self.lex.scan()
                left = left - self.Factor()
            else:
                raise SyntaxError()
        
    def Factor(self):
        left = self.Term()
        while True:
            if self.lex.token in ['+', '-', '\0', ')']:
                return left
            elif self.lex.token == '*':
                self.lex.scan()
                left = left * self.Term()
            elif self.lex.token == '/':
                self.lex.scan()
                left = left / self.Term()
            else:
                raise SyntaxError()
            
    def Term(self):
        if self.lex.token == 'num':
            val = self.lex.match('num')
            return val
        elif self.lex.token == 'var':
            if self.lex.value in self.vars.keys():
                val = self.vars[self.lex.value]
                self.lex.scan()
                return val
            else:
                raise UndefinedError(self.lex.value)
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
            
            
            
            
            
            