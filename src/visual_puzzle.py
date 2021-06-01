import cairo

from puzzle import Puzzle
from style import Style

class VisualPuzzle (Puzzle):

    def __init__ (self, filename, highlights=None):
        super().__init__(filename)
        self.highlights = highlights
    
    def _pre_render (self, style, context):
        pass
    
    def _post_render (self, style, context):
        pass
    
    def render_highlights (self, style, context):
        if not self.highlights: return
        
        r, g, b, a = style.highlight
        context.save()
        context.set_source_rgba(r, g, b, a)
        
        if 'rows' in self.highlights:
            for y in self.highlights['rows']:
                n = style.border + (style.height-2*style.border)/self.size*y
                s = style.border + (style.height-2*style.border)/self.size*(y+1)
                e = style.width - style.border
                w = style.border
                context.save()
                context.move_to(w, n)
                context.line_to(e, n)
                context.line_to(e, s)
                context.line_to(w, s)
                context.close_path()
                context.fill()
                context.restore()
        
        if 'columns' in self.highlights:
            for x in self.highlights['columns']:
                n = style.border
                s = style.width - style.border
                e = style.border + (style.width-2*style.border)/self.size*(x+1)
                w = style.border + (style.width-2*style.border)/self.size*x
                context.save()
                context.move_to(w, n)
                context.line_to(e, n)
                context.line_to(e, s)
                context.line_to(w, s)
                context.close_path()
                context.fill()
                context.restore()
        
        if 'groups' in self.highlights:
            for i in self.highlights['groups']:
                x = i%self.base
                y = i//self.base
                n = style.border + (style.height-2*style.border)/self.size*(y)*self.base
                s = style.border + (style.height-2*style.border)/self.size*(y+1)*self.base
                e = style.border + (style.width-2*style.border)/self.size*(x+1)*self.base
                w = style.border + (style.width-2*style.border)/self.size*(x)*self.base
                context.save()
                context.move_to(w, n)
                context.line_to(e, n)
                context.line_to(e, s)
                context.line_to(w, s)
                context.close_path()
                context.fill()
                context.restore()
        
        context.restore()
        
    
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
        self.render_highlights(style, context)
        
        # lines
        for i in range(self.size+1):
            line_width = style.grid_major_line_width if i%self.base==0 else \
                         style.grid_minor_line_width
            x = border + (width-2*border)/self.size*i
            y = border + (height-2*border)/self.size*i
            
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
        for i in range(self.size):
            for j in range(self.size):
                cell = '' if data[i][j]==-1 else str(data[i][j])
                x = border + (width-2*border)/self.size*(j+0.5)
                y = border + (height-2*border)/self.size*(i+0.5)+textsize/3
                
                context.save()
                context.set_font_size(textsize)
                x_bearing, y_bearing, textwidth, textheight = context.text_extents(cell)[:4]
                context.move_to(x-(x_bearing+textwidth)/2, y)
                context.show_text(cell)
                context.restore()
        
        self._post_render(style, context)

if __name__ == "__main__":
    style = Style()
    
    filename = '../var/samples/example1.txt'
    puzzle = VisualPuzzle(filename);
    puzzle.render('../var/samples/example1.pdf', style)
    
    filename = '../var/samples/example2.txt'
    
    puzzle = VisualPuzzle(filename, {'rows':[6]});
    puzzle.render('../var/samples/example2_row.pdf', style)
    
    puzzle = VisualPuzzle(filename, {'columns':[10]});
    puzzle.render('../var/samples/example2_column.pdf', style)
    
    puzzle = VisualPuzzle(filename, {'groups':[6]});
    puzzle.render('../var/samples/example2_group.pdf', style)
    
    puzzle = VisualPuzzle(filename, {'rows':[6], 'columns':[10], 'groups':[6]});
    puzzle.render('../var/samples/example2_all.pdf', style)
    

