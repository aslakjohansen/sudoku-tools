class Puzzle:
    decode_numeric = {
        '1': 1, '2': 2, '3': 3, '4': 4, 
        '5': 5, '6': 6, '7': 7, '8': 8,
        '9': 9, 'a': 10, 'b': 11, 'c': 12,
        'd': 13, 'e': 14, 'f': 15, '0': 0,
        'g': 16, ' ': -1,
    }
    decode_hex = {
        '1': 1, '2': 2, '3': 3, '4': 4, 
        '5': 5, '6': 6, '7': 7, '8': 8,
        '9': 9, 'a': 'A', 'b': 'B', 'c': 'C',
        'd': 'D', 'e': 'E', 'f': 'F', '0': 0,
        'g': 'G', ' ': -1,
    }
    
    def __init__ (self, filename, decoder=None):
        self.base = 3
        self.encoding = '1byte'
        
        if decoder==None:
          decoder = self.decode_numeric
        
        with open(filename) as fo:
            lines = fo.readlines()
        data = []
        for line in map(lambda line: line.strip('\n'), lines):
            if len(line)>0 and line[0]=='#':
                elements = line.strip().split(' ')
                if   elements[0]=='#base': self.base = int(elements[1])
                elif elements[0]=='#encoding': self.encoding = elements[1]
                continue
            
            ldata = []
            for char in line:
                ldata.append(decoder[char.lower()])
            if len(ldata)!=0:
                data.append(ldata)
        self.data = data
        
        self.size = self.base*self.base
    
    def index (self, x, y):
        if x<0 or x>=self.size: raise Exception('Illegal x value of %s/%s' %(x, type(x)))
        if y<0 or y>=self.size: raise Exception('Illegal y value of %s/%s' %(y, type(y)))
        
        return self.data[y][x]
    
    def validate (self):
        data = self.data
        
        if len(data)!=self.size: return False
        for row in data:
            if len(row)!=self.size: return False
            for cell in row:
                if cell<-1 or cell>self.size: return False
        
        # rows
        for y in range(self.size):
            cells = set()
            for x in range(self.size):
                cell = self.index(x, y)
                if cell==-1: continue
                if cell in cells: return False
                cells.add(cell)
        
        # columns
        for x in range(self.size):
            cells = set()
            for y in range(self.size):
                cell = self.index(x, y)
                if cell==-1: continue
                if cell in cells: return False
                cells.add(cell)
        
        # groups
        for a in range(self.size):
            cells = set()
            for b in range(self.size):
                i = a*self.size+b
                x = i%self.size
                y = i//self.size
                cell = self.index(x, y)
                if cell==-1: continue
                if cell in cells: return False
                cells.add(cell)
        
        return True
        
    def print (self):
        line = ('+'+('-'*self.base))*self.base+'+'
        data = self.data
        for y in range(len(data)):
            row = data[y]
            if y%self.base==0: print(line)
            for x in range(len(row)):
                cell = row[x]
                if x%self.base==0: print('|', end='')
                print(' ' if cell==-1 else cell, end='')
            print('|')
        print(line)

if __name__ == "__main__":
    filename = '../var/samples/example1.txt'
    puzzle = Puzzle(filename);
    print('Validation:', puzzle.validate())
    puzzle.print()

