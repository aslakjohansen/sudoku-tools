import cairo

from puzzle import Puzzle
from style import Style

class VisualPuzzle (Puzzle):

    def __init__ (self, filename):
        super().__init__(filename)
    
    def _pre_render (self, style, context):
        pass
    
    def _post_render (self, style, context):
        pass
    
    def render (self, filename, style, context=None):
        width    = style.width
        height   = style.height
        border   = style.border
        data     = self.data
        textsize = style.textsize
        
        if context==None:
            surface = cairo.PDFSurface(filename, width, height)
            context = cairo.Context(surface)
            context.select_font_face("LMRoman10",
                                     cairo.FONT_SLANT_NORMAL,
                                     cairo.FONT_WEIGHT_NORMAL)
            context.set_font_size(textsize)
        
        self._pre_render(style, context)
        
        # lines
        for i in range(10):
            line_width = style.grid_major_line_width if i%3==0 else \
                         style.grid_minor_line_width
            x = border + (width-2*border)/9*i
            y = border + (height-2*border)/9*i
            
            context.save()
            context.move_to(border, y)
            context.line_to(width-border, y)
            context.move_to(x, border)
            context.line_to(x, height-border)
            context.close_path()
            context.set_line_width(line_width)
            context.set_source_rgb(0, 0, 0)
            context.stroke()
            
        
        # box
        context.save()
        context.move_to(border      , border)
        context.line_to(width-border, border)
        context.line_to(width-border, height-border)
        context.line_to(border      , height-border)
        context.close_path()
        context.set_line_width(style.grid_major_line_width)
        context.set_source_rgb(0, 0, 0)
        context.stroke()
        
        # cells
        for i in range(9):
            for j in range(9):
                cell = '' if data[i][j]==0 else str(data[i][j])
                x = border + (width-2*border)/9*(j+0.5)
                y = border + (height-2*border)/9*(i+0.5)+textsize/3
                
                context.save()
                context.set_font_size(textsize)
                x_bearing, y_bearing, textwidth, textheight = context.text_extents(cell)[:4]
                context.move_to(x-(x_bearing+textwidth)/2, y)
                context.show_text(cell)
                context.restore()
        
        self._post_render(style, context)

if __name__ == "__main__":
    filename = '../var/samples/example1.txt'
    puzzle = VisualPuzzle(filename);
    style = Style()
    puzzle.render('../var/samples/example1.pdf', style)

