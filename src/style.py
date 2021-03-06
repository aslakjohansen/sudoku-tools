
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
        self.compliance_line_width = mm(0.1)
        self.compliance_radius     = mm(0.3)
        self.highlight = (1,0.5,0.5,0.3)

