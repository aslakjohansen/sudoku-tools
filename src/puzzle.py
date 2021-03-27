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
    
    def validate (self):
        data = self.data
        
        if len(data)!=9: return False
        for row in data:
            if len(row)!=9: return False
            for cell in row:
                if cell<0 or cell>9: return False
        
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

