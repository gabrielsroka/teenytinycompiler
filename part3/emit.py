# Emitter object keeps track of the generated code and outputs it.
class Emitter:
    def __init__(self, fullPath, tab=4):
        self.fullPath = fullPath
        self.tab = tab
        self.code = ''
        self.line = ''
        self.indent = 0

    def emit(self, code):
        if self.line == '':
            self.line = ' ' * self.indent * self.tab
        self.line += code

    def emitLine(self, code):
        if code.endswith('}'): self.indent -= 1
        self.emit(code)
        self.code += self.line + '\n'
        self.line = ''
        if code.endswith('{'): self.indent += 1

    def writeFile(self):
        with open(self.fullPath, 'w') as outputFile:
            outputFile.write(self.code)
