class Puzzle:

    def __init__ (self, filename):
        with open(filename) as fo:
            lines = fo.readlines()
        data = []
        for line in map(lambda line: line.strip('\n'), lines):
            ldata = []
            for char in line:
                ldata.append(0 if char==' ' else int(char))
            if len(ldata)!=0:
                data.append(ldata)
        self.data = data
    
    def index (self, x, y):
        if x<0 or x>8: raise Exception('Illegal x value of %s/%s' %(x, type(x)))
        if y<0 or y>8: raise Exception('Illegal y value of %s/%s' %(y, type(y)))
        
        return self.data[y][x]
    
    def validate (self):
        data = self.data
        
        if len(data)!=9: return False
        for row in data:
            if len(row)!=9: return False
            for cell in row:
                if cell<0 or cell>9: return False
        
        # rows
        for y in range(9):
            cells = set()
            for x in range(9):
                cell = self.index(x, y)
                if cell==0: continue
                if cell in cells: return False
                cells.add(cell)
        
        # columns
        for x in range(9):
            cells = set()
            for y in range(9):
                cell = self.index(x, y)
                if cell==0: continue
                if cell in cells: return False
                cells.add(cell)
        
        # groups
        for a in range(9):
            cells = set()
            for b in range(9):
                i = a*9+b
                x = i%9
                y = i//9
                cell = self.index(x, y)
                if cell==0: continue
                if cell in cells: return False
                cells.add(cell)
        
        return True
        
    def print (self):
        data = self.data
        for y in range(len(data)):
            row = data[y]
            if y%3==0: print('+---+---+---+')
            for x in range(len(row)):
                cell = row[x]
                if x%3==0: print('|', end='')
                print(' ' if cell==0 else cell, end='')
            print('|')
        print('+---+---+---+')

if __name__ == "__main__":
    filename = '../var/samples/example1.txt'
    puzzle = Puzzle(filename);
    print('Validation:', puzzle.validate())
    puzzle.print()

