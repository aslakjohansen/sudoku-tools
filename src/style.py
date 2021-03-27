
# convenient conversion functions
def inch (i): return float(i)*72.0
def mm (mm): return inch(float(mm)/25.4)

class Style:
    def __init__ (self):
        self.width  = mm(120)
        self.height = mm(120)
        self.textsize = 18.0
        self.border = mm(1)
        self.grid_major_line_width = mm(0.4)
        self.grid_minor_line_width = mm(0.2)

